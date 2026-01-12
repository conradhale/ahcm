<script setup lang="ts">
import { useData } from "vitepress";
import HomeLogo from "./components/HomeLogo.vue";
import HeaderLogo from "./assets/HeaderLogo.vue";
import SettingsIcon from "./assets/SettingsIcon.vue";
import Gallery from "./components/Gallery.vue";
import { useTemplateRef } from "vue";

const header = useTemplateRef("header");
const content = useTemplateRef("content");

const { frontmatter } = useData();
</script>

<template>
  <header class="header space-between" ref="header">
    <div>
      <a class="logo" href="/"><HeaderLogo class="logo" /></a>
    </div>
    <div>
      <nav>
        <ul>
          <li><a href="/design">design</a></li>
          <li><a href="/about">about</a></li>
          <li><SettingsIcon></SettingsIcon></li>
        </ul>
      </nav>
    </div>
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
      <Gallery
        v-if="frontmatter.gallery"
        :images="frontmatter.gallery.images"
        :cols="frontmatter.gallery.cols ?? 3"
        :categories="frontmatter.gallery.categories ?? []"
      />
      <Content />
    </div>
  </main>
  <footer class="footer">
    <div class="content space-between">
      <div>
        <a class="btn primary" href="mailto://artbyadamh@gmail.com">Email Me</a>
      </div>
      <div>
        <p>&copy; Adam Hale - 2026</p>
      </div>
    </div>
  </footer>
</template>
<style>
:root {
  --header-height: 5em;
  --text-gray: hsl(0 0 77);
  --bg-dark: hsl(0 0 15);
  --bg-light: hsl(0 0 99);

  --fg-light: hsl(0 0 2);

  --btn-fg: hsl(0 0 26);
  --btn-bg: hsl(0 0 99);
  --btn-border: hsl(0 0 87);

  --btn-hover-bg: hsl(0 0 94);
  --btn-hover-fg: hsl(0 0 0);
  --btn-hover-border: hsl(0 0 18);

  --btn-active-bg: hsl(0 0 94);
  --btn-active-fg: hsl(0 0 0);
  --btn-active-border: hsl(0 0 48);

  --primary: hsl(351 100 57);
  --primary-fg: hsl(0 0 99);
}

body {
  background-color: var(--bg-dark);
}

main {
  background-color: var(--bg-light);
  color: var(--fg-light);
}

.space-between {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.header {
  position: sticky;
  top: 0;
  left: 0;
  right: 0;
  z-index: 999;
  background-color: hsl(from var(--bg-dark) h s l / 0.9);
  padding: 1.5em;
  height: var(--header-height);
  backdrop-filter: blur(0.5em);
  max-width: 120em;
  margin-inline: auto;

  > div {
    height: 100%;
    display: flex;
    flex-direction: row;
    align-items: center;
  }

  .logo {
    height: 100%;
    display: flex;
  }

  nav {
    > ul {
      display: inline-flex;
      flex-direction: row;
      gap: 1em;
      list-style-type: none;
    }

    a {
      color: var(--text-gray);
      font-weight: 500;
      text-decoration: none;
      font-size: large;
    }
  }
}

.btn {
  height: 2.5em;
  padding-inline: 1em;
  display: flex;
  align-items: center;
  border-radius: 0.25em;

  a& {
    text-decoration: none;
  }

  &.pill {
    border-radius: 1.25em;
    font-size: large;
  }

  &.primary {
    background-color: var(--primary);
    color: var(--primary-fg);
  }

  &.flat {
    color: var(--btn-fg);
    background-color: var(--btn-bg);
    border: 2px solid var(--btn-border);
    box-shadow: 0 0.05em 0.5em hsl(0 0 0 / 15%);

    &:hover {
      color: var(--btn-hover-fg);
      background-color: var(--btn-hover-bg);
      border-color: var(--btn-hover-border);
    }

    &.active {
      color: var(--btn-active-fg);
      background-color: var(--btn-active-bg);
      border-color: var(--btn-active-border);
    }
  }
}

.content {
  max-width: 80em;
  padding: 2em 3em;
  margin-inline: auto;
}

.page-title {
  font-size: 1.75em;
  margin-bottom: 1em;
  font-weight: 450;
}

.footer {
  background-color: hsl(0 0 85);
  > div {
    align-items: center;
  }
}
</style>
