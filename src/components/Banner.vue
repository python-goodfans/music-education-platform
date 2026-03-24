<template>
  <div class="banner-carousel">
    <div v-for="(banner, index) in banners" :key="index" class="banner-item">
      <img :src="banner.image" :alt="banner.altText" />
      <p>{{ banner.description }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      banners: [
        { image: 'banner1.jpg', altText: 'Banner 1', description: 'Welcome to Music Education!' },
        { image: 'banner2.jpg', altText: 'Banner 2', description: 'Learn from the best!' },
        { image: 'banner3.jpg', altText: 'Banner 3', description: 'Join our community!' },
      ],
    };
  },
  mounted() {
    this.startCarousel();
  },
  methods: {
    startCarousel() {
      let index = 0;
      setInterval(() => {
        const items = document.querySelectorAll('.banner-item');
        items[index].classList.remove('active');
        index = (index + 1) % items.length;
        items[index].classList.add('active');
      }, 3000);
    },
  },
};
</script>

<style scoped>
.banner-carousel {
  position: relative;
  overflow: hidden;
}
.banner-item {
  display: none;
}
.banner-item.active {
  display: block;
}
</style>
