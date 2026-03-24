<template>
  <div class="admin-dashboard">
    <h1>Admin Dashboard</h1>
    <div class="tabs">
      <ul>
        <li v-for="tab in tabs" :key="tab.name" @click="selectTab(tab)">{{ tab.name }}</li>
      </ul>
    </div>
    <div class="tab-content">
      <component :is="activeTabComponent" />
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tabs: [
        { name: 'Users', component: 'UsersTab' },
        { name: 'Articles', component: 'ArticlesTab' },
        { name: 'Files Management', component: 'FilesManagementTab' },
        { name: 'Statistics', component: 'StatisticsTab' }
      ],
      activeTab: null
    };
  },
  computed: {
    activeTabComponent() {
      return this.activeTab ? this.activeTab.component : null;
    }
  },
  methods: {
    selectTab(tab) {
      this.activeTab = tab;
    }
  },
  mounted() {
    this.activeTab = this.tabs[0]; // Set default active tab
  }
};
</script>

<style scoped>
.admin-dashboard {
  padding: 20px;
}
.tabs ul {
  list-style: none;
  padding: 0;
}
.tabs li {
  display: inline-block;
  margin-right: 15px;
  cursor: pointer;
  padding: 10px;
}
.tab-content {
  margin-top: 20px;
}
</style>