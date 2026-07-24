// SkillHub 批量社区发布脚本 (增强版 - 含可见性诊断)
// 在 https://skillhub.cn/admin/skills 页面控制台执行
(async function() {
  const API_HOST = "https://api.skillhub.cn";
  const ORG_ID = 862;
  const PUBLISHER_ID = 742;
  const BATCH_SIZE = 10;  // 每批并发数
  const RESULTS = { published: [], failed: [], renamed: [], visibility_report: {} };
  
  console.log("=== SkillHub 批量社区发布 (增强版) ===");
  
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
  
  // 2. 可见性诊断报告
  const visReport = {
    total: allSkills.length,
    public: 0,
    org_only: 0,
    null_visibility: 0,
    hidden: 0,
    not_download_ready: 0,
    team_namespace: 0,
    global_namespace: 0,
    invisible_reasons: []
  };
  
  allSkills.forEach(s => {
    if (s.visibility === 'public') visReport.public++;
    else if (s.visibility === 'org_only') visReport.org_only++;
    else visReport.null_visibility++;
    
    if (s.hidden === true) {
      visReport.hidden++;
      visReport.invisible_reasons.push({ slug: s.slug, reason: 'hidden' });
    }
    
    if (s.latestVersion && s.latestVersion.download_ready === false) {
      visReport.not_download_ready++;
      visReport.invisible_reasons.push({ slug: s.slug, reason: 'download_not_ready' });
    }
    
    if (s.namespace && s.namespace.type === 'TEAM' && s.visibility !== 'public') {
      visReport.team_namespace++;
      visReport.invisible_reasons.push({ slug: s.slug, reason: 'team_namespace_not_public' });
    } else if (s.namespace && s.namespace.type === 'GLOBAL') {
      visReport.global_namespace++;
    }
  });
  
  console.log("\n=== 可见性诊断报告 ===");
  console.log(`  public: ${visReport.public}`);
  console.log(`  org_only: ${visReport.org_only}`);
  console.log(`  null_visibility: ${visReport.null_visibility}`);
  console.log(`  hidden: ${visReport.hidden}`);
  console.log(`  not_download_ready: ${visReport.not_download_ready}`);
  console.log(`  TEAM namespace: ${visReport.team_namespace}`);
  console.log(`  GLOBAL namespace: ${visReport.global_namespace}`);
  if (visReport.invisible_reasons.length > 0) {
    console.log(`\n  不可见原因 (${visReport.invisible_reasons.length} 个):`);
    visReport.invisible_reasons.slice(0, 20).forEach(r => 
      console.log(`    ${r.slug}: ${r.reason}`));
  }
  RESULTS.visibility_report = visReport;
  
  // 3. 筛选需要发布的skill (org_only + null visibility)
  const toPublish = allSkills.filter(s => 
    s.visibility === 'org_only' || !s.visibility);
  console.log(`\n需要发布(org_only + null): ${toPublish.length} 个`);
  
  if (toPublish.length === 0) {
    console.log("✅ 所有skill已对外发布!");
    window.__publishResults = RESULTS;
    console.log("结果已保存到 window.__publishResults");
    return;
  }
  
  // 4. 批量发布
  for (let i = 0; i < toPublish.length; i += BATCH_SIZE) {
    const batch = toPublish.slice(i, i + BATCH_SIZE);
    console.log(`处理批次 ${Math.floor(i/BATCH_SIZE)+1}: ${i+1}-${Math.min(i+BATCH_SIZE, toPublish.length)}/${toPublish.length}`);
    
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
    if (i + BATCH_SIZE < toPublish.length) {
      await new Promise(r => setTimeout(r, 500));
    }
  }
  
  // 5. 输出结果
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
  console.log("\n结果已保存到 window.__publishResults (含可见性诊断报告)");
  console.log("复制结果: JSON.stringify(window.__publishResults)");
})();
