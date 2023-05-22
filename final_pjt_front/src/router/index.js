import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/Movies/HomeView'
import ChooseView from '../views/Movies/ChooseView'
import AloneMovieView from '../views/Movies/AloneMovieView'
import LoverMovieView from '../views/Movies/LoverMovieView'
import FriendMovieView from '../views/Movies/FriendMovieView'
import FamilyMovieView from '../views/Movies/FamilyMovieView'
import NormalMovieView from '../views/Movies/NormalMovieView'
import RandomMovieView from '../views/Movies/RandomMovieView'
import MovieDetailView from '../views/Movies/MovieDetailView'

// community 관련
import CommunityView from '../views/Community/CommunityView'
import FreeCommunityView from '../views/Community/FreeCommunityView'
import TogetherCommunityView from '../views/Community/TogetherCommunityView'
import FreeCreateView from '../views/Community/FreeCreateView'
import TogetherCreateView from '../views/Community/TogetherCreateView'
import FreeDetailView from '../views/Community/FreeDetailView'
import TogetherDetailView from '../views/Community/TogetherDetailView'


// 로그인 관련
import LoginView from '../views/Accounts/LoginView'
import SignupView from '../views/Accounts/SignupView'
import ProfileView from '../views/Accounts/ProfileView'


// 404
import NotFoundView from '../views/NotFoundView'

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
    component: ChooseView,
    meta: {
      requiresAuth: true
    }
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
    path: '/choosefriend',
    name: 'FriendMovieView',
    component: FriendMovieView
  },
  {
    path: '/choosefamily',
    name: 'FamilyMovieView',
    component: FamilyMovieView
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
    path: '/movies/:pk',
    name: 'MovieDetailView',
    component: MovieDetailView,
  },


  // 회원관리
  {
    path: '/login',
    name: 'LoginView',
    component: LoginView
  },
  {
    path: '/signup',
    name: 'SignupView',
    component: SignupView
  },
  {
    path: '/profile/:userid',
    name: 'ProfileView',
    component: ProfileView,
  },
  // community
  {
    path: '/community',
    name: 'CommunityView',
    component: CommunityView,
    children: [
      {
        path: '/together',
        name: 'TogetherCommunityView',
        component: TogetherCommunityView
      },
      //
      {
        path: '/togethercreate',
        name: 'TogetherCreateView',
        component: TogetherCreateView
      },
      {
        path: '/free',
        name: 'FreeCommunityView',
        component: FreeCommunityView
      },
      {
        path: '/freecreate',
        name: 'FreeCreateView',
        component: FreeCreateView
      },
    ]
  },
  {
    path: '/free/:freepk',
    name: 'FreeDetailView',
    component: FreeDetailView
  },
  //
  {
    path: '/together/:togetherpk',
    name: 'TogetherDetailView',
    component: TogetherDetailView
  },


  // 404 not found
  {
    path: '/404',
    name: 'NotFound',
    component: NotFoundView
  },
  {
    path: '*',
    redirect: '/404',
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
