<script setup lang="ts">
import { useData, useRouter } from "vitepress";
import { ref, computed, onBeforeMount } from "vue";
const props = defineProps<{
  categories?: { [key: string]: string };
  images: {
    src: string;
    label: string;
    category?: string;
  }[];
  cols: number;
}>();

const router = useRouter();

const url = new URL(location.href);

const selectedCategory = ref<string | null>(url.searchParams.get("category") ?? null);

const images = computed(() =>
  selectedCategory.value === null
    ? props.images
    : props.images.filter((img) => img.category === selectedCategory.value),
);

const setCategory = (category: string | null) => {
  if (category === null) {
    url.searchParams.delete("category");
  } else {
    url.searchParams.set("category", category);
  }
  router.go(url.toString());

  selectedCategory.value = category;
};
</script>
<template>
  <div v-if="props.categories" class="categories">
    <button
      class="btn pill flat"
      :class="selectedCategory === null ? 'active' : ''"
      @click="setCategory(null)"
    >
      All
    </button>
    <button
      v-for="(category, key) in categories"
      class="btn pill flat"
      :class="selectedCategory === key ? 'active' : ''"
      @click="setCategory(key)"
    >
      {{ category }}
    </button>
  </div>
  <ul class="gallery">
    <li v-for="{ src, label } in images">
      <figure>
        <img :src="`/${src}`" />
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

  grid-template-columns: repeat(v-bind("props.cols"), 1fr);
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
