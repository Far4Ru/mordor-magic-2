import Vue from 'vue'
import VueRouter from 'vue-router'

// импортируем все представления, по
// которым будем навигировать пользователя
import Greeting from '@/views/Greeting.vue'
import Main from '@/views/Main.vue'

Vue.use(VueRouter)

// заводим массив с роутами
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
  } /*
  {
    path: '/registration',
    name: 'Registration',
    component: Registration
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile
  },
  {
    path: '/messages',
    name: 'Messages',
    component: Messages
  },
  {
    path: '/messages',
    name: 'Messages',
    component: Messages
  },
  {
    path: '/info',
    name: 'Info',
    component: Info
  },
  {
    path: '/members',
    name: 'Members',
    component: Members
  },
  {
    path: '/events',
    name: 'Events',
    component: Events
  } */
]

// создаём новый экземпляр класса
// VueRouter, с необходимыми параметрами
const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// экспортируем сконфигурированный роутер
export default router
