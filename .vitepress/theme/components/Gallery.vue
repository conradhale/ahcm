<script setup lang="ts">
import { ref, computed } from 'vue'
const props = defineProps<{
  categories?: string[]
  images: {
    src: string
    label: string
    category?: number
  }[]
  cols: number
}>()

const selectedCategory = ref<number | null>(null)

const images = computed(() => selectedCategory.value === null ? props.images : props.images.filter(img => img.category === selectedCategory.value))

</script>
<template>
<div v-if="props.categories" class="categories">
  <button
    class="btn-pill"
    :class="selectedCategory === null ? 'active' : ''"
    @click="() => selectedCategory = null">All</button>
  <button
    v-for="category, idx in categories"
    class="btn-pill"
    :class="selectedCategory === idx ? 'active' : ''"
    @click="() => selectedCategory = idx"
  >
    {{ category }}
  </button>
</div>
<ul class="gallery">
  <li v-for="{src, label} in images">
    <figure>
      <img :src="`/${src}`"></img>
      <figcaption>{{ label }}</figcaption>
    </figure>
  </li>
</ul>
</template>
<style>
.gallery {
  --gallery-gap: 1em;

  display: grid;
  grid-gap: var(--gallery-gap);

  grid-template-columns: repeat(v-bind('props.cols'), 1fr);
  margin: auto;

  list-style-type: none;
  margin: 0;
  padding: 0;

  li {
    display: inline-block;
  }

  img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    aspect-ratio: 1 / 1;
  }
}

.categories {
  display: flex;
  flex-direction: row;
  gap: 1em;
  margin-block-end: 2em;
}
</style>
