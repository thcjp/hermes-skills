# 详细参考 - frontend-design-v3-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (tsx)

```tsx
// React + TypeScript + Framer Motion 生产级组件
import { motion, useScroll, useTransform } from 'framer-motion';
import { lazy, Suspense } from 'react';
import type { FC } from 'react';

// 设计令牌
const tokens = {
  color: {
    bgPrimary: '#0a0a0a',
    bgSecondary: '#1a1a2e',
    accent: '#c8553d',
    text: '#f5f1e8',
    textMuted: '#8b8378',
  },
  font: {
    heading: "'Playfair Display', serif",
    body: "'IBM Plex Sans', sans-serif",
    mono: "'JetBrains Mono', monospace",
  },
  space: { sm: '0.5rem', md: '1rem', lg: '2rem', xl: '4rem' },
} as const;

// 可访问性: 语义化 + ARIA
interface HeroSectionProps {
  title: string;
  subtitle: string;
  onCTAClick?: () => void;
}

export const HeroSection: FC<HeroSectionProps> = ({
  title,
  subtitle,
  onCTAClick,
}) => {
  const { scrollY } = useScroll();
  const opacity = useTransform(scrollY, [0, 300], [1, 0]);
  const y = useTransform(scrollY, [0, 300], [0, -50]);

  return (
    <section
      aria-labelledby="hero-title"
      style={{
        background: tokens.color.bgPrimary,
        minHeight: '90vh',
        display: 'flex',
        alignItems: 'center',
        padding: tokens.space.xl,
      }}
    >
      <motion.div
        style={{ opacity, y }}
        initial="hidden"
        animate="visible"
        variants={{
          hidden: {},
          visible: { transition: { staggerChildren: 0.15 } },
        }}
      >
        <motion.h1
          id="hero-title"
          variants={{
            hidden: { opacity: 0, y: 40 },
            visible: { opacity: 1, y: 0 },
          }}
          transition={{ duration: 0.8, ease: [0.22, 1, 0.36, 1] }}
          style={{
            fontFamily: tokens.font.heading,
            fontSize: 'clamp(2.5rem, 6vw, 5rem)',
            fontWeight: 900,
            lineHeight: 1.05,
            color: tokens.color.text,
          }}
        >
          {title}
        </motion.h1>

        <motion.p
          variants={{
            hidden: { opacity: 0, y: 30 },
            visible: { opacity: 1, y: 0 },
          }}
          style={{
            fontFamily: tokens.font.body,
            fontSize: '1.125rem',
            color: tokens.color.textMuted,
            maxWidth: '32rem',
            marginTop: tokens.space.md,
          }}
        >
          {subtitle}
        </motion.p>

        <motion.button
          variants={{
            hidden: { opacity: 0, y: 20 },
            visible: { opacity: 1, y: 0 },
          }}
          whileHover={{ scale: 1.05 }}
          whileTap={{ scale: 0.98 }}
          onClick={onCTAClick}
          aria-label="主要操作按钮"
          style={{
            marginTop: tokens.space.lg,
            padding: `${tokens.space.md} ${tokens.space.lg}`,
            background: tokens.color.accent,
            color: tokens.color.text,
            border: 'none',
            borderRadius: '8px',
            fontFamily: tokens.font.body,
            fontSize: '1rem',
            fontWeight: 600,
            cursor: 'pointer',
          }}
        >
          开始探索
        </motion.button>
      </motion.div>
    </section>
  );
};

// 懒加载的次屏组件
const LazyGallery = lazy(() => import('./Gallery'));

export const Page: FC = () => {
  return (
    <>
      <HeroSection
        title="设计的可能性"
        subtitle="用独特的审美拒绝平庸的AI风格"
      />
      <Suspense fallback={<div aria-busy="true">加载中...</div>}>
        <LazyGallery />
      </Suspense>
    </>
  );
};
```

## 代码示例 (vue)

```vue
<!-- Vue 3 + Composition API + TypeScript -->
<template>
  <section
    ref="sectionRef"
    aria-labelledby="feature-title"
    class="feature-section"
  >
    <TransitionGroup name="stagger" tag="div" class="feature-grid">
      <article
        v-for="(feature, index) in features"
        :key="feature.id"
        class="feature-card"
        :style="{ '--stagger-delay': `${index * 0.1}s` }"
      >
        <h3 :id="feature.id">{{ feature.title }}</h3>
        <p>{{ feature.description }}</p>
      </article>
    </TransitionGroup>
  </section>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';

interface Feature {
  id: string;
  title: string;
  description: string;
}

const sectionRef = ref<HTMLElement>();
const features = ref<Feature[]>([
  { id: 'f1', title: '独特美学', description: '拒绝通用AI风格' },
  { id: 'f2', title: '生产级代码', description: 'TypeScript类型安全' },
  { id: 'f3', title: '可访问性', description: 'WCAG 2.1 AA合规' },
]);

// 滚动驱动动效
onMounted(() => {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
        }
      });
    },
    { threshold: 0.1 }
  );

  if (sectionRef.value) {
    observer.observe(sectionRef.value);
  }
});
</script>

<style scoped>
.feature-section {
  background: #0a0a0a;
  padding: 4rem 2rem;
}

.feature-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

.feature-card {
  background: #1a1a2e;
  border: 1px solid rgba(200, 85, 61, 0.2);
  border-radius: 12px;
  padding: 2rem;
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.6s ease, transform 0.6s ease;
}

.visible .feature-card {
  opacity: 1;
  transform: translateY(0);
  transition-delay: var(--stagger-delay, 0s);
}

.feature-card h3 {
  font-family: 'Playfair Display', serif;
  font-size: 1.5rem;
  color: #f5f1e8;
  margin-bottom: 0.5rem;
}

.feature-card p {
  font-family: 'IBM Plex Sans', sans-serif;
  color: #8b8378;
  font-size: 0.9rem;
}
</style>
```

