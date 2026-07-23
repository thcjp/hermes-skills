// SkillHub COS失败重试脚本 (自动生成)
// 在 https://skillhub.cn/admin/skills 页面控制台执行
(async function() {
  const API_HOST = "https://api.skillhub.cn";
  const ORG_ID = 862;
  const PUBLISHER_ID = 742;
  const COS_FAILURE_SLUGS = ["communication-skill-free", "cloud-free", "cloud-architect-free", "clawcall-free", "chart-free", "can-free", "calendar-reminder-free", "bookmark-intelligence-free", "bilibili-helper-free", "bilibili-all-in-one-free", "beware-piper-tts-free", "azure-ai-voicelive-py-free", "azure-ai-transcription-py-free", "api-integration-free", "api-generator-free", "api-gateway-free", "api-free", "api-doc-writer-free", "anygen-diagram-generator-free", "anthropics-frontend-design-free", "alibaba-quark-scan-free", "alephnet-node-free", "aic-dashboard-free", "ai-assistant-free", "ai-assistant", "ai-agent-helper-free", "agentvibes-voice-skill-free", "agentvibes-voice-skill", "agentvibes-content-skill", "agent-telegram-free", "admapix-free", "claude-code-delegate-free", "baidu-netdisk-skills-free", "azure-infra-free", "azure-cloud-architect-free", "aws-infra-free", "aws-graph-agent-free", "automation-recipe-pack", "aegis-security-free", "ad-insight-hub-free"];
  const RESULTS = { published: [], failed: [] };
  
  console.log(`=== COS失败重试: ${COS_FAILURE_SLUGS.length} 个skill ===`);
  
  for (let i = 0; i < COS_FAILURE_SLUGS.length; i++) {
    const slug = COS_FAILURE_SLUGS[i];
    console.log(`[${i+1}/${COS_FAILURE_SLUGS.length}] 重试: ${slug}`);
    
    try {
      const resp = await fetch(`${API_HOST}/api/v1/orgs/${ORG_ID}/admin/skills/${slug}/publish-to-community`, {
        method: 'POST',
        credentials: 'include',
        headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        body: JSON.stringify({ publisherProfileId: PUBLISHER_ID })
      });
      const data = await resp.json().catch(() => ({}));
      
      if (resp.ok) {
        RESULTS.published.push(slug);
        console.log(`  ✅ 成功`);
      } else {
        RESULTS.failed.push({ slug, error: data.error || `HTTP_${resp.status}` });
        console.log(`  ❌ 失败: ${data.error || resp.status}`);
      }
    } catch(e) {
      RESULTS.failed.push({ slug, error: e.message });
      console.log(`  ❌ 异常: ${e.message}`);
    }
    
    // 请求间隔
    if (i + 1 < COS_FAILURE_SLUGS.length) {
      await new Promise(r => setTimeout(r, 300));
    }
  }
  
  console.log("\n=== 重试结果 ===");
  console.log(`✅ 成功: ${RESULTS.published.length}`);
  console.log(`❌ 失败: ${RESULTS.failed.length}`);
  
  if (RESULTS.failed.length > 0) {
    console.log("\n仍失败的skill:");
    RESULTS.failed.forEach(f => console.log(`  ${f.slug}: ${f.error}`));
  }
  
  window.__cosRetryResults = RESULTS;
  console.log("\n结果已保存到 window.__cosRetryResults");
})();
