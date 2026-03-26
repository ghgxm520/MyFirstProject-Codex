import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '../views/home/HomeView.vue'
import AdminDashboard from '../views/admin/AdminDashboard.vue'

const routes = [
  { path: '/', component: HomeView },
  { path: '/admin', component: AdminDashboard }
]

export default createRouter({
  history: createWebHistory(),
  routes
})
