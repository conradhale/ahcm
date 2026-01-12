<script setup lang="ts">
import { DotLottieVue, DotLottieVueInstance } from "@lottiefiles/dotlottie-vue";
import { useTemplateRef, onMounted, reactive } from "vue";
import DownArrowIcon from "../assets/DownArrowIcon.vue";

const props = defineProps<{
  header: HTMLElement;
  after: HTMLElement;
}>();

const renderConfig = reactive({ devicePixelRatio: window.devicePixelRatio, autoResize: true });

window.addEventListener("resize", () => {
  renderConfig.devicePixelRatio = window.devicePixelRatio;
});

const hero = useTemplateRef("hero");
const skip_to_content = useTemplateRef("skip-to-content");

const start = 399;
const end = 540;

const logo = useTemplateRef<DotLottieVueInstance>("logo");
onMounted(() => {
  const lottie = logo.value?.getDotLottieInstance();

  function scrollHandler(e: Event) {
    if (!hero.value || !lottie) {
      return;
    }
    const frame = Math.round(window.scrollY / 3) + start;
    if (frame < end) {
      if (lottie.isPlaying) {
        lottie.pause();
        lottie.setSegment(start, end);
      }
      lottie.setFrame(frame);
    }
  }

  document.addEventListener("scroll", scrollHandler);
  document.addEventListener("scrollend", scrollHandler);

  skip_to_content.value?.addEventListener("click", () => {
    window.scrollTo({
      top:
        props.after.getBoundingClientRect().top +
        window.scrollY -
        props.header.getBoundingClientRect().height,
      behavior: "smooth",
    });
  });
});
</script>
<template>
  <div class="hero" ref="hero">
    <DotLottieVue
      ref="logo"
      autoplay
      useFrameInterpolation
      :renderConfig="renderConfig"
      src="logo.lottie"
      :segment="[0, start]"
      :layout="{ fit: 'fit-height' }"
    />
    <h1 class="visually-hidden">Adam Hale</h1>
    <p class="visually-hidden">
      Creating logical design systems informed by creative art. Designed to be practical,
      user-focused, and innovative.
    </p>

    <button aria-label="Skip to content" class="skip-to-content" ref="skip-to-content">
      <DownArrowIcon></DownArrowIcon>
    </button>
  </div>
</template>
<style>
.hero {
  width: 100vw;
  height: 150vh;
  position: relative;
  height: calc(100vh - var(--header-height));

  > div {
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    width: 100%;
    margin: auto;
  }

  .skip-to-content {
    display: inline-flex;
    bottom: 0;
    z-index: 1;
    left: calc(50% - 8em);
    position: absolute;
    width: 8em;
    height: 4em;
    border-radius: 4em 4em 0 0;
    border: 0;
    margin-bottom: -2px;
    border-bottom-color: white;
    background-color: white;
    padding-block-start: 1em;
    justify-content: center;
    align-items: center;
  }
}
</style>
