import Vue from 'vue'
import Vuex from 'vuex'

import createPersistedState from 'vuex-persistedstate'

import axios from 'axios'
import router from '@/router'
const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)


export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    token: null,
    userInfo: null,
    articles: [],
    reviews: [],
    selectMovie: null,

  },
  getters: {
    isLogin: (state) => state.token ? true: false,
    authHeader: (state) => ({Authorization: `Token ${state.token}`}),
    articles: (state) => state.articles,
    reviews: (state) => state.reviews,
    selectMovie(state) {
      return state.selectMovie
    }
  },
  mutations: {
    // signup & login -> 완료하면 토큰 발급
    SET_TOKEN(state, token) {
      state.token = token
      router.push({name : 'HomeView'}).catch(() => {})
    },
    SET_USERINFO: (state, userInfo) => state.userInfo = userInfo,

    GET_ARTICLES(state, articles) {
      state.articles = articles
    },
    GET_REVIEWS(state, reviews) {
      state.reviews = reviews
    },
    GET_ARTICLES_TOGETHER(state, articlesTogether) {
      state.articlesTogether = articlesTogether
    },
    DELETE_ARTICLE(state, article) {
      const index = state.articles.findIndex(a => a.id === article.id)
      if (index !== -1) {
        state.articles.splice(index, 1)
      }
    },
    DELETE_ARTICLE_TOGETHER(state, articlesTogether) {
      const index = state.articlesTogether.findIndex(a => a.id === articlesTogether.id)
      if (index !== -1) {
        state.articlesTogether.splice(index, 1)
      }
    },
    SET_RESULT_MOVIE(state, movie) {
      // state.resultMovie.push(movie)
      // state.resultMovie = [...state.resultMovie, movie]
      state.selectMovie = movie
    },
  },
  actions: {
    signUp(context, data) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data,
      })
        .then(res => {
          console.log(res)
          context.commit('SET_TOKEN', res.data.key)
          context.dispatch('getUserInfo') 
  
        })
        .catch(err => {
          console.log(err.response.data)
          if (err.response.data.non_field_errors == "The two password fields didn't match.") {
            alert('비밀번호가 일치하지 않음')
          } else if (err.response.data.username == 'A user with that username already exists.') {
            alert('이미 존재하는 아이디임')
          } else if (err.response.data.password1 == "This password is too short. It must contain at least 8 characters.") {
            alert('비밀번호 넘 짧음 -0- ;;;')
          }
        })       
    },
    login(context, data) {      
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data,
      })
        .then(res => {
          console.log(res)
          context.commit('SET_TOKEN', res.data.key)
          context.dispatch('getUserInfo')
          router.push({name: 'HomeView'}).catch(() => {})
        })
        .catch((err) => {console.log(err)
        alert('아이디나 비밀번호 틀렸어욧 -0-;;;')})      
    },
    getUserInfo({getters, commit}) {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user/`,
        headers: getters.authHeader
      })
        .then(res => {
          console.log(res)
          commit('SET_USERINFO', res.data)
        })
        .catch(err => console.log(err))
    },
    logout({commit, getters}) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/logout/`,
        headers: getters.authHeader
      })
        .then(res => {
          console.log(res)
          commit('SET_TOKEN', '')
          commit('SET_USERINFO', null)
          router.push({name: 'HomeView'}).catch(() => {})

        })
        .catch(err => console.log(err))
    },
    getArticles(context) {
        axios({
          method: 'get',
          url: `${API_URL}/community/free/`,
          headers: context.getters.authHeader
        })
          .then((res) => {
            context.commit('GET_ARTICLES', res.data)
          })
          .catch((err) => {
            console.log(err)
            console.log('get에서 오류남!!!!')
          })
    },
    getArticlesTogether(context) {
      axios({
        method: 'get',
        url: `${API_URL}/community/together/`,
        headers: context.getters.authHeader
      })
        .then((res) => {
          context.commit('GET_ARTICLES_TOGETHER', res.data)
        })
        .catch((err) => {
          console.log(err)
          console.log('TOGETHER에 넣는 데이터가 오류남')
        })
    },


    getReviews(context, movie_id) {
        const movieId = movie_id
        axios({
          method: 'get',
          url: `${API_URL}/movies/review/${movieId}/`,
          headers: context.getters.authHeader
        })
          .then((res) => {
            context.commit('GET_REVIEWS', res.data)
            console.log(res.data, '이거나옴?')
          })
          .catch((err) => {
            console.log(err)
            console.log('get에서 오류남!!!!')
          })
    },
    setResultMovie({ commit }, movie) {
      commit('SET_RESULT_MOVIE', movie)
    },

  },
})


