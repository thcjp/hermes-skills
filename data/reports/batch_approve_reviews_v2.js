// SkillHub 批量审核通过脚本 v2
// 在 https://www.skillhub.cn/admin/skill-reviews 页面控制台执行
(async function() {
  const API_HOST = "https://api.skillhub.cn";
  const ORG_ID = 862;
  const BATCH_SIZE = 5;
  let approved = 0;
  let failed = 0;
  let totalProcessed = 0;

  // localStorage进度持久化
  const STORAGE_KEY = 'skillhub_approve_progress';
  let progress = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');
  let startPage = progress.lastPage || 1;

  console.log("=== SkillHub 批量审核通过 v2 ===");
  console.log(`从第 ${startPage} 页开始（已处理 ${progress.totalProcessed || 0} 个）`);

  function saveProgress(page, processed) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify({
      lastPage: page,
      totalProcessed: processed
    }));
  }

  const allButtons = document.querySelectorAll('button');
  const approveButtons = Array.from(allButtons).filter(b => b.textContent.trim() === '审核通过');
  const totalPages = document.querySelectorAll('[class*="page"], [class*="Page"]');

  console.log(`当前页面有 ${approveButtons.length} 个审核按钮`);

  for (let i = 0; i < approveButtons.length; i++) {
    try {
      approveButtons[i].click();
      approved++;
      totalProcessed++;
      console.log(`  [${totalProcessed}] 审核通过已点击`);

      await new Promise(r => setTimeout(r, 500));

      const newButtons = document.querySelectorAll('button');
      const newApproveButtons = Array.from(newButtons).filter(b => b.textContent.trim() === '审核通过');
      if (newApproveButtons.length > 0 && i < approveButtons.length - 1) {
        approveButtons.length = 0;
        approveButtons.push(...newApproveButtons);
        i = -1;
      }
    } catch(e) {
      failed++;
      console.error(`  审核失败: ${e.message}`);
    }

    if (totalProcessed % BATCH_SIZE === 0) {
      console.log(`已处理 ${totalProcessed} 个, 成功 ${approved}, 失败 ${failed}`);
      saveProgress(startPage, totalProcessed);
      await new Promise(r => setTimeout(r, 1000));
    }
  }

  saveProgress(startPage + 1, totalProcessed);
  console.log(`\n=== 完成 ===`);
  console.log(`总计处理: ${totalProcessed}`);
  console.log(`成功: ${approved}`);
  console.log(`失败: ${failed}`);
  console.log(`\n请刷新页面继续处理下一页`);
})();
