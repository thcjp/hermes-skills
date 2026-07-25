// SkillHub 批量审核通过脚本 v3
// 在 https://www.skillhub.cn/admin/skill-reviews 页面控制台执行
// 增强: 自动检测总页数 + 智能翻页 + 进度保存 + 错误恢复
(async function() {
  'use strict';

  // ===== 配置 =====
  const BATCH_DELAY = 300;        // 每个审核点击间隔(ms)
  const PAGE_DELAY = 1500;        // 翻页延迟(ms)
  const SAVE_INTERVAL = 10;       // 每N个保存一次进度
  const PROGRESS_KEY = 'sh_approve_v3_progress';

  // ===== 状态 =====
  let totalApproved = 0;
  let totalFailed = 0;
  let totalSkipped = 0;
  let currentPage = 1;
  let totalPages = 1;

  // 恢复进度
  const saved = localStorage.getItem(PROGRESS_KEY);
  if (saved) {
    try {
      const p = JSON.parse(saved);
      totalApproved = p.approved || 0;
      totalFailed = p.failed || 0;
      totalSkipped = p.skipped || 0;
      currentPage = p.page || 1;
      console.log(`%c恢复进度: 通过${totalApproved}, 失败${totalFailed}, 跳过${totalSkipped}, 从第${currentPage}页继续`, 'color: #00a4ff; font-size: 14px;');
    } catch(e) {
      console.log('进度恢复失败，从头开始');
    }
  }

  console.log('%c=== SkillHub 批量审核通过 v3 ===', 'color: #0052d9; font-size: 16px; font-weight: bold;');

  // ===== 工具函数 =====
  function sleep(ms) {
    return new Promise(r => setTimeout(r, ms));
  }

  function getApproveButtons() {
    // 查找所有"审核通过"按钮
    return Array.from(document.querySelectorAll('button, a'))
      .filter(b => {
        const text = b.textContent.trim();
        return text === '审核通过' || text === '通过';
      });
  }

  function getTotalPages() {
    // 从分页组件获取总页数
    const pageButtons = Array.from(document.querySelectorAll('button'))
      .filter(b => {
        const text = b.textContent.trim();
        return /^第?\s*\d+\s*页?$/.test(text) || /^\d+$/.test(text);
      })
      .map(b => parseInt(b.textContent.replace(/[^\d]/g, '')))
      .filter(n => !isNaN(n) && n > 0);

    if (pageButtons.length > 0) {
      return Math.max(...pageButtons);
    }

    // 从文本中提取 "共 XXX 条" 和每页数量
    const text = document.body.innerText;
    const totalMatch = text.match(/共\s*(\d+)\s*条/);
    if (totalMatch) {
      const total = parseInt(totalMatch[1]);
      return Math.ceil(total / 10); // 每页10条
    }

    return 271; // 默认值
  }

  function getTotalRecords() {
    const text = document.body.innerText;
    const match = text.match(/共\s*(\d+)\s*条/);
    return match ? parseInt(match[1]) : 0;
  }

  async function goToPage(pageNum) {
    // 方法1: 直接点击页码按钮
    const pageBtn = Array.from(document.querySelectorAll('button'))
      .find(b => {
        const text = b.textContent.trim();
        return text === String(pageNum) || text === `第 ${pageNum} 页` || text === `第${pageNum}页`;
      });

    if (pageBtn && !pageBtn.disabled) {
      pageBtn.click();
      await sleep(PAGE_DELAY);
      return true;
    }

    // 方法2: 点击"下一页"
    if (pageNum === currentPage + 1) {
      const nextBtn = Array.from(document.querySelectorAll('button'))
        .find(b => b.textContent.includes('下一页') && !b.disabled);
      if (nextBtn) {
        nextBtn.click();
        await sleep(PAGE_DELAY);
        return true;
      }
    }

    // 方法3: 使用URL导航
    const url = new URL(window.location.href);
    url.searchParams.set('page', pageNum);
    window.history.pushState({}, '', url);
    window.location.reload();
    await sleep(3000);
    return true;
  }

  function saveProgress() {
    localStorage.setItem(PROGRESS_KEY, JSON.stringify({
      approved: totalApproved,
      failed: totalFailed,
      skipped: totalSkipped,
      page: currentPage,
      timestamp: Date.now()
    }));
  }

  // ===== 获取总页数 =====
  totalPages = getTotalPages();
  const totalRecords = getTotalRecords();
  console.log(`总记录: ${totalRecords}, 总页数: ${totalPages}`);
  console.log(`从第 ${currentPage} 页开始处理\n`);

  // ===== 主循环 =====
  for (let page = currentPage; page <= totalPages; page++) {
    console.log(`\n%c--- 第 ${page}/${totalPages} 页 ---`, 'color: #00a4ff; font-weight: bold;');

    await sleep(PAGE_DELAY);

    // 获取审核按钮
    let buttons = getApproveButtons();
    console.log(`  找到 ${buttons.length} 个审核按钮`);

    if (buttons.length === 0) {
      // 可能页面还没加载完，等待重试
      await sleep(2000);
      buttons = getApproveButtons();
      if (buttons.length === 0) {
        console.log(`  ⚠️ 无审核按钮，可能已全部处理`);
        totalSkipped++;
      }
    }

    // 逐个点击审核通过
    for (let i = 0; i < buttons.length; i++) {
      try {
        const btn = buttons[i];
        if (btn.disabled || btn.classList.contains('disabled')) {
          totalSkipped++;
          continue;
        }

        btn.click();
        totalApproved++;
        await sleep(BATCH_DELAY);

        // 检查是否出现确认对话框
        const confirmBtn = Array.from(document.querySelectorAll('button'))
          .find(b => b.textContent.trim() === '确认' || b.textContent.trim() === '确定');
        if (confirmBtn) {
          confirmBtn.click();
          await sleep(500);
        }
      } catch(e) {
        totalFailed++;
        console.log(`  ❌ 第${i+1}个失败: ${e.message}`);
      }

      // 定期保存进度
      if ((totalApproved + totalFailed) % SAVE_INTERVAL === 0) {
        saveProgress();
        console.log(`  📊 进度: 通过${totalApproved}, 失败${totalFailed}, 跳过${totalSkipped}`);
      }
    }

    // 保存当前页进度
    saveProgress();

    // 翻到下一页
    if (page < totalPages) {
      const moved = await goToPage(page + 1);
      if (!moved) {
        console.log('%c⚠️ 无法翻页，尝试刷新...', 'color: #e8a200;');
        window.location.reload();
        await sleep(3000);
      }
      currentPage = page + 1;
    }
  }

  // ===== 清理和报告 =====
  localStorage.removeItem(PROGRESS_KEY);

  console.log('\n%c=== 审核完成 ===', 'color: #0052d9; font-size: 16px; font-weight: bold;');
  console.log(`%c✅ 总通过: ${totalApproved}`, 'color: #007e3e; font-size: 14px;');
  console.log(`%c❌ 总失败: ${totalFailed}`, 'color: #c92a2a; font-size: 14px;');
  console.log(`%c⏭️ 总跳过: ${totalSkipped}`, 'color: #868e96; font-size: 14px;');
  console.log(`%c📊 处理页面: ${totalPages}`, 'color: #0052d9; font-size: 14px;');

  // 返回汇总
  return {
    approved: totalApproved,
    failed: totalFailed,
    skipped: totalSkipped,
    pages: totalPages
  };
})();
