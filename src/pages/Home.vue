<template>
  <div>
    <Banner />
    <CardCarousel />
    <div class="features">
      <h2>Features</h2>
      <ul>
        <li>Feature 1</li>
        <li>Feature 2</li>
        <li>Feature 3</li>
      </ul>
    </div>
  </div>
</template>

<script>
import Banner from '@/components/Banner.vue';
import CardCarousel from '@/components/CardCarousel.vue';

export default {
  components: {
    Banner,
    CardCarousel,
  },
};
</script>

<style scoped>
.features {
  margin-top: 20px;
}
</style>