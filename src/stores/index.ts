import { createPinia } from 'pinia';

export const pinia = createPinia();

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    token: '',
    isAuthenticated: false,
  }),
  actions: {
    setUser(user) {
      this.user = user;
      this.isAuthenticated = !!user;
    },
    setToken(token) {
      this.token = token;
      this.isAuthenticated = !!token;
    },
    clearAuth() {
      this.user = null;
      this.token = '';
      this.isAuthenticated = false;
    },
  },
});