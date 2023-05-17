import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import CommunityView from '../views/CommunityView.vue'
import AccountView from '../views/AccountView.vue'
import MovieView from '../views/MovieView.vue'
import ChooseView from '../views/ChooseView.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView
  },
  {
    path: '/community',
    name: 'CommunityView',
    component: CommunityView
  },
  {
    path: '/login',
    name: 'AccountView',
    component: AccountView
  },
  {
    path: '/movie',
    name: 'MovieView',
    component: MovieView
  },
  {
    path: '/choose',
    name: 'ChooseView',
    component: ChooseView
  },


]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
