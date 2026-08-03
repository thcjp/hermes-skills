/* === unified-fix-plan charts.js ===
   ECharts chart definitions for the unified fix plan report.
   Theme: dark (#0f1117 / #1a1d28 / #e8eaf0)
   Charts:
     1) Critical/High issue trend across 5 review rounds (bar)
     2) 18-step implementation timeline (horizontal bar / gantt)
     3) Problem distribution pie (pricing / data / fragmentation / platform)
*/

(function () {
  'use strict';

  /* ---- Shared theme tokens ---- */
  var COLORS = {
    bg: '#0f1117',
    bg2: '#1a1d28',
    ink: '#e8eaf0',
    muted: '#8b90a0',
    rule: '#2a2e3a',
    accent: '#4f9eff',
    accent2: '#f0a040',
    danger: '#ef4444',
    ok: '#10b981',
    warn: '#facc15'
  };

  var FONT_FAMILY = "'InstrumentSans','WorkSans',system-ui,sans-serif";
  var MONO_FAMILY = "'GeistMono',monospace";

  /* ---- Common axis / text style ---- */
  function axisLabelStyle() {
    return { color: COLORS.ink, fontFamily: FONT_FAMILY, fontSize: 12 };
  }
  function splitLineStyle() {
    return { lineStyle: { color: COLORS.rule, type: 'dashed' } };
  }

  /* =========================================================
     Chart 1 — 5轮审核 Critical / High 问题递减趋势（柱状图）
     ========================================================= */
  function renderReviewTrend(dom) {
    var chart = echarts.init(dom, null, { renderer: 'canvas' });
    var option = {
      backgroundColor: 'transparent',
      color: [COLORS.danger, COLORS.accent2],
      tooltip: {
        trigger: 'axis',
        backgroundColor: COLORS.bg2,
        borderColor: COLORS.rule,
        textStyle: { color: COLORS.ink, fontFamily: FONT_FAMILY },
        axisPointer: { type: 'shadow', shadowStyle: { color: 'rgba(79,158,255,0.08)' } }
      },
      legend: {
        data: ['Critical', 'High'],
        top: 8,
        textStyle: { color: COLORS.ink, fontFamily: FONT_FAMILY, fontSize: 13 },
        itemWidth: 14,
        itemHeight: 14,
        itemGap: 24
      },
      grid: { left: 56, right: 28, top: 56, bottom: 48 },
      xAxis: {
        type: 'category',
        data: ['R1 架构师', 'R2 数据安全', 'R3 实施可行性', 'R4 完整性', 'R5 CTO最终'],
        axisLine: { lineStyle: { color: COLORS.rule } },
        axisTick: { show: false },
        axisLabel: axisLabelStyle()
      },
      yAxis: {
        type: 'value',
        name: '问题数量',
        nameTextStyle: { color: COLORS.muted, fontFamily: FONT_FAMILY, fontSize: 12 },
        axisLine: { show: false },
        axisTick: { show: false },
        axisLabel: axisLabelStyle(),
        splitLine: splitLineStyle()
      },
      series: [
        {
          name: 'Critical',
          type: 'bar',
          barWidth: 22,
          barGap: '20%',
          itemStyle: {
            borderRadius: [4, 4, 0, 0],
            color: {
              type: 'linear', x: 0, y: 0, x2: 0, y2: 1,
              colorStops: [
                { offset: 0, color: '#ef4444' },
                { offset: 1, color: 'rgba(239,68,68,0.55)' }
              ]
            }
          },
          label: {
            show: true, position: 'top',
            color: COLORS.ink, fontFamily: FONT_FAMILY, fontSize: 12, fontWeight: 600
          },
          data: [5, 3, 4, 5, 0]
        },
        {
          name: 'High',
          type: 'bar',
          barWidth: 22,
          itemStyle: {
            borderRadius: [4, 4, 0, 0],
            color: {
              type: 'linear', x: 0, y: 0, x2: 0, y2: 1,
              colorStops: [
                { offset: 0, color: '#f0a040' },
                { offset: 1, color: 'rgba(240,160,64,0.55)' }
              ]
            }
          },
          label: {
            show: true, position: 'top',
            color: COLORS.ink, fontFamily: FONT_FAMILY, fontSize: 12, fontWeight: 600
          },
          data: [12, 5, 3, 8, 1]
        }
      ]
    };
    chart.setOption(option);
    return chart;
  }

  /* =========================================================
     Chart 2 — 18步实施计划时间线（水平条形 / 甘特图）
     ========================================================= */
  function renderTimeline(dom) {
    var chart = echarts.init(dom, null, { renderer: 'canvas' });

    /* step data: [label, startDay, durationDay, phaseTag, isCritical] */
    var steps = [
      ['18 端到端管道测试',           24.25, 1.00, 'Phase 5b',     false],
      ['17 测试用例编写',             20.75, 3.50, 'Phase 5a',     false],
      ['16 平台抽象层',               17.25, 3.50, 'Phase 4.1-4.3', false],
      ['15 quality_dashboard迁移',    16.75, 0.50, '补充',          false],
      ['14 L2/L3/L4分层检查统一',     15.25, 1.50, 'Phase 3.10',   false],
      ['13 统一评分/评估体系',        11.75, 3.50, 'Phase 3.9',    false],
      ['12 统一占位符检测规则',       10.75, 1.00, 'Phase 3.12',   false],
      ['11 统一extract_section()',    10.75, 1.00, 'Phase 3.11',   false],
      ['10 代码去碎片化(3.2-3.8)',     8.25, 2.50, 'Phase 3.2-3.8', false],
      ['09 统一DB路径',                8.00, 0.25, 'Phase 2.3',    false],
      ['08 消除JSON双写(47处)',        4.50, 3.50, 'Phase 2.2',    true],
      ['07 统一定价引擎+表重构',       2.50, 2.00, 'Phase 1.1+1.2', false],
      ['06 修复回填逻辑',              2.25, 0.25, 'Phase 2.4',    false],
      ['05 新建SQLite表+schema版本',   1.25, 1.00, 'Phase 2.1+2.6', false],
      ['04 统一API URL',               0.75, 0.50, 'Phase 3.1',    false],
      ['03 建立回归基线',              0.625, 0.125, 'Phase 0c',   false],
      ['02 搭建测试基础设施',          0.125, 0.50, 'Phase 0b',    true],
      ['01 修复busy_timeout',          0.00, 0.125, 'Phase 0a',    true]
    ];

    var categories = steps.map(function (s) { return s[0]; });

    var barColor = function (isCritical) {
      return isCritical ? COLORS.danger : COLORS.accent;
    };

    var option = {
      backgroundColor: 'transparent',
      tooltip: {
        trigger: 'axis',
        backgroundColor: COLORS.bg2,
        borderColor: COLORS.rule,
        textStyle: { color: COLORS.ink, fontFamily: FONT_FAMILY },
        axisPointer: { type: 'shadow', shadowStyle: { color: 'rgba(79,158,255,0.06)' } },
        formatter: function (params) {
          var idx = params[0].dataIndex;
          var s = steps[idx];
          return '<b>' + s[0].replace(/^\d+\s/, '') + '</b><br/>' +
                 'Phase: ' + s[3] + '<br/>' +
                 '开始: 第 ' + s[1].toFixed(2) + ' 天<br/>' +
                 '工期: ' + s[2].toFixed(2) + ' 天' +
                 (s[4] ? '<br/><span style="color:#ef4444">关键路径</span>' : '');
        }
      },
      legend: { show: false },
      grid: { left: 190, right: 60, top: 16, bottom: 48 },
      xAxis: {
        type: 'value',
        name: '工作日',
        nameLocation: 'middle',
        nameGap: 32,
        nameTextStyle: { color: COLORS.muted, fontFamily: FONT_FAMILY, fontSize: 12 },
        axisLine: { lineStyle: { color: COLORS.rule } },
        axisTick: { show: false },
        axisLabel: axisLabelStyle(),
        splitLine: splitLineStyle(),
        min: 0,
        max: 27
      },
      yAxis: {
        type: 'category',
        data: categories,
        inverse: true,
        axisLine: { lineStyle: { color: COLORS.rule } },
        axisTick: { show: false },
        axisLabel: {
          color: COLORS.ink,
          fontFamily: FONT_FAMILY,
          fontSize: 11,
          width: 170,
          overflow: 'truncate'
        }
      },
      series: [
        {
          name: 'offset',
          type: 'bar',
          stack: 'gantt',
          barWidth: 14,
          barGap: '10%',
          z: 0,
          itemStyle: { color: 'transparent' },
          emphasis: { itemStyle: { color: 'transparent' } },
          data: steps.map(function (s) { return s[1]; }),
          tooltip: { show: false },
          silent: true
        },
        {
          name: '工期',
          type: 'bar',
          stack: 'gantt',
          barWidth: 14,
          data: steps.map(function (s) {
            return {
              value: s[2],
              itemStyle: {
                borderRadius: 3,
                color: barColor(s[4])
              }
            };
          }),
          label: {
            show: true,
            position: 'right',
            color: COLORS.muted,
            fontFamily: FONT_FAMILY,
            fontSize: 10,
            formatter: function (p) {
              var s = steps[p.dataIndex];
              return s[2] >= 1 ? s[2].toFixed(1) + '天' : (s[2] * 8).toFixed(0) + 'h';
            }
          }
        }
      ]
    };

    chart.setOption(option);
    return chart;
  }

  /* =========================================================
     Chart 3 — 问题分布饼图（定价 / 数据 / 碎片化 / 平台抽象）
     ========================================================= */
  function renderProblemPie(dom) {
    var chart = echarts.init(dom, null, { renderer: 'canvas' });
    var option = {
      backgroundColor: 'transparent',
      color: [COLORS.danger, COLORS.accent, COLORS.accent2, COLORS.ok],
      tooltip: {
        trigger: 'item',
        backgroundColor: COLORS.bg2,
        borderColor: COLORS.rule,
        textStyle: { color: COLORS.ink, fontFamily: FONT_FAMILY },
        formatter: '{b}<br/>问题数: {c} ({d}%)'
      },
      legend: {
        orient: 'vertical',
        right: 16,
        top: 'center',
        textStyle: { color: COLORS.ink, fontFamily: FONT_FAMILY, fontSize: 13 },
        itemWidth: 12,
        itemHeight: 12,
        itemGap: 18
      },
      series: [
        {
          name: '问题分布',
          type: 'pie',
          radius: ['42%', '68%'],
          center: ['38%', '50%'],
          avoidLabelOverlap: true,
          itemStyle: {
            borderColor: COLORS.bg,
            borderWidth: 3,
            borderRadius: 6
          },
          label: {
            show: true,
            color: COLORS.ink,
            fontFamily: FONT_FAMILY,
            fontSize: 13,
            fontWeight: 600,
            formatter: '{b}\n{c}'
          },
          labelLine: {
            lineStyle: { color: COLORS.rule },
            length: 12,
            length2: 16
          },
          emphasis: {
            label: { fontSize: 15, fontWeight: 700 },
            itemStyle: { shadowBlur: 16, shadowColor: 'rgba(0,0,0,0.45)' }
          },
          data: [
            { value: 6,  name: '定价体系冲突' },
            { value: 20, name: '数据跟踪问题' },
            { value: 12, name: '代码碎片化' },
            { value: 4,  name: '平台抽象问题' }
          ]
        }
      ]
    };
    chart.setOption(option);
    return chart;
  }

  /* ---- Resize handling ---- */
  var instances = [];
  function register(charts) {
    instances = charts.filter(Boolean);
    window.addEventListener('resize', function () {
      instances.forEach(function (c) { c.resize(); });
    });
  }

  /* ---- Boot ---- */
  function boot() {
    if (typeof echarts === 'undefined') {
      console.error('[charts.js] echarts is not loaded.');
      return;
    }
    var t1 = document.getElementById('chart-review-trend');
    var t2 = document.getElementById('chart-timeline');
    var t3 = document.getElementById('chart-problem-pie');
    register([t1 && renderReviewTrend(t1), t2 && renderTimeline(t2), t3 && renderProblemPie(t3)]);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
