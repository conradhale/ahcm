<script setup lang="ts">
import { useTemplateRef, onMounted, ref } from 'vue'
import { useData } from 'vitepress'

import HeaderLogo from './HeaderLogo.vue'
import logo from './logo.json'
import logo_bg from './logo_bg.json'

import lottie from 'lottie-web'

const header = useTemplateRef('header')

const hero = useTemplateRef('hero')
const hero_logo = useTemplateRef('hero-logo')
const hero_logo_bg = useTemplateRef('hero-logo-bg')

onMounted(() => {
  const logo_bg_animation = lottie.loadAnimation({
    container: hero_logo_bg.value, // the dom element that will contain the animation
    renderer: 'svg',
    loop: false,
    autoplay: true,
    animationData: logo_bg,
    initialSegment: [0, 283],
    rendererSettings: {
      preserveAspectRatio: 'xMidYMid slice'
    }
  })

  const logo_animation = lottie.loadAnimation({
    container: hero_logo.value, // the dom element that will contain the animation
    renderer: 'svg',
    loop: false,
    autoplay: true,
    animationData: logo,
    initialSegment: [0, 283],
    rendererSettings: {
      preserveAspectRatio: 'xMidYMid meet'
    }
  })

  const observer = new IntersectionObserver((entries, observer) => {
    for (const entry of entries) {
      if (entry.boundingClientRect.height > 0 && entry.intersectionRatio < 0.9) {
        observer.disconnect()
        logo_animation.playSegments([291, 465])
        logo_bg_animation.playSegments([291, 465])
      }
      break
    }
  }, {
    threshold: [0.9]
  })

  observer.observe(hero.value)
})

// https://vitepress.dev/reference/runtime-api#usedata
const { site, frontmatter } = useData()
</script>

<template>
  <header class="header" ref="header">
    <HeaderLogo class="logo"/>
  </header>
  <div v-if="frontmatter.home">
    <div class="hero" ref="hero">
      <div class="logo-bg" ref="hero-logo-bg"></div>
      <div class="logo" ref="hero-logo"></div>
    </div>

    <h1>{{ site.title }}</h1>
    <p>{{ site.description }}</p>
    <ul>
    </ul>
  </div>
  <div v-else>
    <a href="/">Home</a>
    <Content />
  </div>
  <div style="height: 1000px;"></div>
</template>
