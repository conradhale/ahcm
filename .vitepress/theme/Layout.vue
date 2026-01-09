<script setup lang="ts">
import { useData } from 'vitepress'
import HomeLogo from './components/HomeLogo.vue';
import HeaderLogo from './assets/HeaderLogo.vue'
import Gallery from './components/Gallery.vue';
import { useTemplateRef } from 'vue';

const header = useTemplateRef('header')
const content = useTemplateRef('content')

// https://vitepress.dev/reference/runtime-api#usedata
const { site, frontmatter } = useData()
</script>

<template>
  <header class="header" ref="header">
    <a href="/"><HeaderLogo class="logo"/></a>
  </header>
  <main>
    <div v-if="frontmatter.home">
      <HomeLogo :header="header!" :after="content!" />
    </div>
    <div v-else>
      <a href="/">Home</a>
    </div>
    <div class="content" ref="content">
      <h2 v-if="frontmatter.title" class="page-title">{{ frontmatter.title }}</h2>
      <Gallery v-if="frontmatter.gallery" :images="frontmatter.gallery.images" :cols="frontmatter.gallery.cols ?? 3" :categories="frontmatter.gallery.categories ?? []" />
      <Content />
    </div>
  </main>
</template>
