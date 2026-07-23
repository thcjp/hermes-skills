// SkillHub 批量社区发布脚本 (自动生成)
// 在 https://skillhub.cn/admin/skills 页面控制台执行
(async function() {
  const API_HOST = "https://api.skillhub.cn";
  const ORG_ID = 862;
  const PUBLISHER_ID = 742;
  const BATCH_SIZE = 10;  // 每批并发数
  const RESULTS = { published: [], failed: [], renamed: [] };
  
  console.log("=== SkillHub 批量社区发布 ===");
  
  // 1. 获取所有skill
  const allSkills = [];
  let page = 1;
  while (true) {
    const resp = await fetch(`${API_HOST}/api/v1/orgs/${ORG_ID}/admin/skills?page=${page}&pageSize=100`, {
      credentials: 'include',
      headers: { 'Accept': 'application/json' }
    });
    const data = await resp.json();
    if (!data.skills || data.skills.length === 0) break;
    allSkills.push(...data.skills);
    if (allSkills.length >= data.total) break;
    page++;
  }
  console.log(`总共 ${allSkills.length} 个skill`);
  
  // 2. 筛选org_only
  const orgOnly = allSkills.filter(s => s.visibility === 'org_only');
  console.log(`未对外发布(org_only): ${orgOnly.length} 个`);
  console.log(`已对外发布(public): ${allSkills.length - orgOnly.length} 个`);
  
  if (orgOnly.length === 0) {
    console.log("✅ 所有skill已对外发布!");
    return;
  }
  
  // 3. 批量发布
  for (let i = 0; i < orgOnly.length; i += BATCH_SIZE) {
    const batch = orgOnly.slice(i, i + BATCH_SIZE);
    console.log(`处理批次 ${Math.floor(i/BATCH_SIZE)+1}: ${i+1}-${Math.min(i+BATCH_SIZE, orgOnly.length)}/${orgOnly.length}`);
    
    const promises = batch.map(async (skill) => {
      const slug = skill.slug;
      try {
        // 尝试直接发布
        const resp = await fetch(`${API_HOST}/api/v1/orgs/${ORG_ID}/admin/skills/${slug}/publish-to-community`, {
          method: 'POST',
          credentials: 'include',
          headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
          body: JSON.stringify({ publisherProfileId: PUBLISHER_ID })
        });
        const data = await resp.json().catch(() => ({}));
        
        if (resp.status === 200 || resp.status === 201) {
          RESULTS.published.push(slug);
          return { slug, success: true };
        } else if (resp.status === 409 && (data.error === 'slug_conflict' || JSON.stringify(data).includes('slug'))) {
          // slug冲突, 重命名后重试
          const newSlug = slug + '-sk';
          const renameResp = await fetch(`${API_HOST}/api/v1/orgs/${ORG_ID}/admin/skills/${slug}/rename-slug`, {
            method: 'PUT',
            credentials: 'include',
            headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
            body: JSON.stringify({ newSlug })
          });
          
          if (renameResp.ok) {
            // 用新slug重新发布
            const retryResp = await fetch(`${API_HOST}/api/v1/orgs/${ORG_ID}/admin/skills/${newSlug}/publish-to-community`, {
              method: 'POST',
              credentials: 'include',
              headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
              body: JSON.stringify({ publisherProfileId: PUBLISHER_ID })
            });
            
            if (retryResp.ok) {
              RESULTS.published.push(newSlug);
              RESULTS.renamed.push({ original: slug, renamed: newSlug });
              return { slug: newSlug, success: true, renamed_from: slug };
            } else {
              const retryData = await retryResp.json().catch(() => ({}));
              RESULTS.failed.push({ slug, error: retryData.error || `rename_ok_publish_failed_${retryResp.status}` });
              return { slug, success: false, error: retryData.error };
            }
          } else {
            RESULTS.failed.push({ slug, error: 'rename_failed' });
            return { slug, success: false, error: 'rename_failed' };
          }
        } else {
          RESULTS.failed.push({ slug, error: data.error || `HTTP_${resp.status}` });
          return { slug, success: false, error: data.error || `HTTP_${resp.status}` };
        }
      } catch(e) {
        RESULTS.failed.push({ slug, error: e.message });
        return { slug, success: false, error: e.message };
      }
    });
    
    await Promise.all(promises);
    console.log(`  已发布: ${RESULTS.published.length}, 失败: ${RESULTS.failed.length}`);
    
    // 批次间短暂等待
    if (i + BATCH_SIZE < orgOnly.length) {
      await new Promise(r => setTimeout(r, 500));
    }
  }
  
  // 4. 输出结果
  console.log("\n=== 发布结果 ===");
  console.log(`✅ 成功发布: ${RESULTS.published.length}`);
  console.log(`❌ 发布失败: ${RESULTS.failed.length}`);
  console.log(`📝 重命名: ${RESULTS.renamed.length}`);
  
  if (RESULTS.failed.length > 0) {
    console.log("\n失败详情:");
    RESULTS.failed.forEach(f => console.log(`  ${f.slug}: ${f.error}`));
  }
  
  // 保存结果到window供复制
  window.__publishResults = RESULTS;
  console.log("\n结果已保存到 window.__publishResults");
  console.log("复制结果: JSON.stringify(window.__publishResults)");
})();
