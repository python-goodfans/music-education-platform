<template>
  <div class="user-profile">
    <h1>User Profile</h1>
    <button @click="logout">Logout</button>
    <FileManagerComponent />
  </div>
</template>

<script>
import FileManagerComponent from '@/components/FileManagerComponent.vue';

export default {
  components: {
    FileManagerComponent,
  },
  methods: {
    logout() {
      // Implement logout functionality
      console.log('User logged out');
    },
  },
};
</script>

<style scoped>
.user-profile {
  padding: 20px;
}
</style>