import Vue from 'vue'
import VueRouter from 'vue-router'

import Greeting from '@/views/Greeting.vue'
import Main from '@/views/Main.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Greeting',
    component: Greeting
  },
  {
    path: '/home',
    name: 'Home',
    component: Main
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
