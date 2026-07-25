// SkillHub 批量审核通过脚本 v2
// 在 https://www.skillhub.cn/admin/skill-reviews 页面控制台执行
// 功能：自动翻页 + 批量审核通过 + 进度记录
(async function() {
  const API_HOST = "https://api.skillhub.cn";
  const ORG_ID = 862;
  let totalApproved = 0;
  let totalFailed = 0;
  let currentPage = 1;
  let totalPages = 271;
  let processedSlugs = new Set();

  // 从localStorage恢复进度
  const savedProgress = localStorage.getItem('sh_approve_progress');
  if (savedProgress) {
    const progress = JSON.parse(savedProgress);
    totalApproved = progress.approved || 0;
    totalFailed = progress.failed || 0;
    processedSlugs = new Set(progress.slugs || []);
    currentPage = progress.page || 1;
    console.log(`恢复进度: 已通过${totalApproved}, 已失败${totalFailed}, 当前页${currentPage}`);
  }

  console.log("=== SkillHub 批量审核通过 v2 ===");
  console.log(`起始页: ${currentPage}, 总页数: ${totalPages}`);

  // 获取当前页所有审核项
  function getReviewItems() {
    const rows = document.querySelectorAll('table tr, [class*="row"]');
    const items = [];

    // 方法1: 从表格行获取
    const tableRows = document.querySelectorAll('table tbody tr, [class*="table"] [class*="row"]');
    tableRows.forEach(row => {
      const text = row.innerText;
      const approveBtn = row.querySelector('button[class*="approve"], button[onclick*="approve"]');
      const buttons = row.querySelectorAll('button');
      const approveButton = Array.from(buttons).find(b => b.textContent.trim() === '审核通过');
      if (approveButton) {
        items.push({ button: approveButton, row: row, text: text });
      }
    });

    // 方法2: 如果方法1没找到，从全局按钮获取
    if (items.length === 0) {
      const allButtons = document.querySelectorAll('button');
      const approveButtons = Array.from(allButtons).filter(b => b.textContent.trim() === '审核通过');
      approveButtons.forEach(btn => {
        items.push({ button: btn, row: null, text: '' });
      });
    }

    return items;
  }

  // 点击审核通过并等待
  async function clickApprove(button) {
    try {
      button.click();
      await new Promise(r => setTimeout(r, 300));
      return true;
    } catch(e) {
      console.error('点击失败:', e.message);
      return false;
    }
  }

  // 翻到下一页
  async function goToNextPage() {
    const nextBtn = document.querySelector('button[aria-label*="下一页"], button[class*="next"]');
    if (!nextBtn || nextBtn.disabled) {
      // 尝试通过页码按钮翻页
      const pageButtons = document.querySelectorAll('button[class*="page"]');
      const currentPageBtn = Array.from(pageButtons).find(b => b.textContent.trim() === String(currentPage));
      if (currentPageBtn) {
        const nextPageBtn = currentPageBtn.nextElementSibling;
        if (nextPageBtn) {
          nextPageBtn.click();
          await new Promise(r => setTimeout(r, 1500));
          return true;
        }
      }
      return false;
    }
    nextBtn.click();
    await new Promise(r => setTimeout(r, 1500));
    return true;
  }

  // 主循环
  for (let page = currentPage; page <= totalPages; page++) {
    console.log(`\n--- 处理第 ${page}/${totalPages} 页 ---`);

    // 等待页面加载
    await new Promise(r => setTimeout(r, 500));

    // 获取当前页审核项
    const items = getReviewItems();
    console.log(`第${page}页找到 ${items.length} 个审核项`);

    if (items.length === 0) {
      console.log('未找到审核项，尝试等待...');
      await new Promise(r => setTimeout(r, 2000));
      const retryItems = getReviewItems();
      if (retryItems.length === 0) {
        console.log('仍无审核项，跳到下一页');
      } else {
        // 处理重试找到的项
        for (const item of retryItems) {
          const success = await clickApprove(item.button);
          if (success) {
            totalApproved++;
          } else {
            totalFailed++;
          }
          await new Promise(r => setTimeout(r, 200));
        }
      }
    }

    // 逐个审核
    for (let i = 0; i < items.length; i++) {
      const success = await clickApprove(items[i].button);
      if (success) {
        totalApproved++;
      } else {
        totalFailed++;
      }

      // 每10个保存一次进度
      if ((totalApproved + totalFailed) % 10 === 0) {
        localStorage.setItem('sh_approve_progress', JSON.stringify({
          approved: totalApproved,
          failed: totalFailed,
          page: page,
          slugs: Array.from(processedSlugs)
        }));
        console.log(`进度: 已通过${totalApproved}, 失败${totalFailed}, 页${page}`);
      }
    }

    // 翻到下一页
    if (page < totalPages) {
      const moved = await goToNextPage();
      if (!moved) {
        console.log('无法翻到下一页，结束');
        break;
      }
    }
  }

  // 清除进度
  localStorage.removeItem('sh_approve_progress');

  console.log(`\n=== 批量审核完成 ===`);
  console.log(`总通过: ${totalApproved}`);
  console.log(`总失败: ${totalFailed}`);
  console.log(`处理页数: ${totalPages}`);
})();
