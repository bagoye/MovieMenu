import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/Movies/HomeView'
import ChooseView from '../views/Movies/ChooseView'
import AloneMovieView from '../views/Movies/AloneMovieView'
import LoverMovieView from '../views/Movies/LoverMovieView'
import NormalMovieView from '../views/Movies/NormalMovieView'
import RandomMovieView from '../views/Movies/RandomMovieView'
import CommunityView from '../views/CommunityView'
import AccountView from '../views/AccountView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView
  },
  {
    path: '/choose',
    name: 'ChooseView',
    component: ChooseView
  },
  {
    path: '/choosealone',
    name: 'AloneMovieView',
    component: AloneMovieView
  },
  {
    path: '/chooselover',
    name: 'LoverMovieView',
    component: LoverMovieView
  },
  {
    path: '/normal',
    name: 'NormalMovieView',
    component: NormalMovieView
  },
  {
    path: '/momakase',
    name: 'RandomMovieView',
    component: RandomMovieView
  },
  {
    path: '/community',
    name: 'CommunityView',
    component: CommunityView
  },
  {
    path: '/account',
    name: 'AccountView',
    component: AccountView
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
