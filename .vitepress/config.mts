import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "AHCM",
  description: "Adam Hale Creative Media",
  head: [
    ['link', {rel: 'preconnect', href: 'https://rsms.me/'}],
    ['link', {rel: 'stylesheet', href: 'https://rsms.me/inter/inter.css'}],
  ]
})
