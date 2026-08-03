(function() {
  var style = getComputedStyle(document.documentElement);
  var accent = style.getPropertyValue('--accent').trim();
  var accent2 = style.getPropertyValue('--accent2').trim();
  var ink = style.getPropertyValue('--ink').trim();
  var muted = style.getPropertyValue('--muted').trim();
  var rule = style.getPropertyValue('--rule').trim();
  var bg2 = style.getPropertyValue('--bg2').trim();
  var danger = style.getPropertyValue('--danger').trim();
  var warn = style.getPropertyValue('--warn').trim();
  var ok = style.getPropertyValue('--ok').trim();

  // --- Chart 1: Pricing Comparison (Log Scale) ---
  var chart1 = echarts.init(document.getElementById('chart-pricing-compare'), null, { renderer: 'svg' });
  chart1.setOption({
    title: {
      text: '单次调用定价对比（元/次，对数坐标）',
      left: 'center',
      textStyle: { color: ink, fontSize: 14, fontWeight: 600 }
    },
    tooltip: {
      trigger: 'axis',
      appendToBody: true,
      axisPointer: { type: 'shadow' },
      formatter: function(params) {
        var html = '';
        params.forEach(function(p) {
          html += p.seriesName + ': ' + p.value + ' 元/次<br/>';
        });
        return html;
      }
    },
    legend: {
      data: ['本项目定价', 'Coze插件定价'],
      bottom: 0,
      textStyle: { color: muted, fontSize: 12 }
    },
    grid: { left: '8%', right: '8%', bottom: '15%', top: '15%' },
    xAxis: {
      type: 'category',
      data: ['基础工具类', '图像处理类', '音乐生成类', '高级/专业类'],
      axisLine: { lineStyle: { color: rule } },
      axisLabel: { color: muted, fontSize: 11 }
    },
    yAxis: {
      type: 'log',
      name: '元/次',
      nameTextStyle: { color: muted, fontSize: 11 },
      axisLine: { lineStyle: { color: rule } },
      axisLabel: { color: muted, fontSize: 11 },
      splitLine: { lineStyle: { color: rule, type: 'dashed' } }
    },
    series: [
      {
        name: '本项目定价',
        type: 'bar',
        data: [9.9, 19.9, 29.9, 99.9],
        itemStyle: { color: accent, borderRadius: [4, 4, 0, 0] },
        barWidth: '30%',
        label: {
          show: true,
          position: 'top',
          color: ink,
          fontSize: 11,
          formatter: '{c}元'
        }
      },
      {
        name: 'Coze插件定价',
        type: 'bar',
        data: [0.01, 0.025, 1.0, 1.0],
        itemStyle: { color: accent2, borderRadius: [4, 4, 0, 0] },
        barWidth: '30%',
        label: {
          show: true,
          position: 'top',
          color: ink,
          fontSize: 11,
          formatter: '{c}元'
        }
      }
    ],
    animation: false
  });
  window.addEventListener('resize', function() { chart1.resize(); });

  // --- Chart 2: Data Count Comparison ---
  var chart2 = echarts.init(document.getElementById('chart-data-compare'), null, { renderer: 'svg' });
  chart2.setOption({
    title: {
      text: '本地记录 vs 平台实际（个）',
      left: 'center',
      textStyle: { color: ink, fontSize: 14, fontWeight: 600 }
    },
    tooltip: {
      trigger: 'axis',
      appendToBody: true,
      axisPointer: { type: 'shadow' }
    },
    legend: {
      data: ['本地记录', '平台实际'],
      bottom: 0,
      textStyle: { color: muted, fontSize: 12 }
    },
    grid: { left: '10%', right: '8%', bottom: '15%', top: '15%' },
    xAxis: {
      type: 'category',
      data: ['ClawHub', 'SkillHub'],
      axisLine: { lineStyle: { color: rule } },
      axisLabel: { color: muted, fontSize: 13 }
    },
    yAxis: {
      type: 'value',
      name: '数量',
      nameTextStyle: { color: muted, fontSize: 11 },
      axisLine: { lineStyle: { color: rule } },
      axisLabel: { color: muted, fontSize: 11 },
      splitLine: { lineStyle: { color: rule, type: 'dashed' } }
    },
    series: [
      {
        name: '本地记录',
        type: 'bar',
        data: [
          { value: 1496, itemStyle: { color: warn } },
          { value: 1120, itemStyle: { color: warn } }
        ],
        barWidth: '25%',
        label: {
          show: true,
          position: 'top',
          color: ink,
          fontSize: 13,
          fontWeight: 600
        },
        markPoint: {
          data: [
            { name: '虚高+526', coord: [0, 1496], itemStyle: { color: danger }, label: { color: '#fff', fontSize: 11 } },
            { name: '虚低-880+', coord: [1, 1120], itemStyle: { color: danger }, label: { color: '#fff', fontSize: 11 } }
          ],
          symbolSize: 60
        }
      },
      {
        name: '平台实际',
        type: 'bar',
        data: [
          { value: 970, itemStyle: { color: danger } },
          { value: 2035, itemStyle: { color: danger } }
        ],
        barWidth: '25%',
        label: {
          show: true,
          position: 'top',
          color: ink,
          fontSize: 13,
          fontWeight: 600
        }
      }
    ],
    animation: false
  });
  window.addEventListener('resize', function() { chart2.resize(); });

  // --- Mermaid Init ---
  if (typeof mermaid !== 'undefined') {
    mermaid.initialize({
      startOnLoad: true,
      theme: 'dark',
      themeVariables: {
        primaryColor: '#1a1d28',
        primaryTextColor: '#e8eaf0',
        primaryBorderColor: '#4f9eff',
        lineColor: '#8b92a8',
        secondaryColor: '#232838',
        tertiaryColor: '#2d3344',
        fontFamily: 'WorkSans, Microsoft YaHei, sans-serif'
      },
      securityLevel: 'loose'
    });
  }
})();
