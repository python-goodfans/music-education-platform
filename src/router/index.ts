import Vue from 'vue';
import Router from 'vue-router';
import Home from '../views/Home.vue';
import About from '../views/About.vue';

Vue.use(Router);

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/about',
      name: 'About',
      component: About,
    },
  ],
});

// Navigation Guards
router.beforeEach((to, from, next) => {
  // Add your authentication logic here
  const isAuthenticated = false; // Replace this with actual authentication check
  if (to.matched.some(record => record.meta.requiresAuth) && !isAuthenticated) {
    next({ name: 'Home' }); // Redirect to Home if not authenticated
  } else {
    next(); // Proceed to the route
  }
});

export default router;