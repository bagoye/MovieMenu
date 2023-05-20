
import axios from 'axios'
import router from '@/router'
const API_URL = 'http://127.0.0.1:8000'


export default {
  state: {
    articles: [
    ],
    token: null,
    userInfo: null,
  },
  getters: {
    isLogin: (state) => state.token ? true: false,
    authHeader: (state) => ({Authorization: `Token ${state.token}`}),
  },
  mutations: {

    // signup & login -> 완료하면 토큰 발급
    SET_TOKEN(state, token) {
      state.token = token
      router.push({name : 'HomeView'}).catch(() => {}) // store/index.js $router 접근 불가 -> import를 해야함
    },

    SET_USERINFO: (state, userInfo) => state.userInfo = userInfo,

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
        .catch(err => console.log(err))
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
        .catch(err => console.log(err))      
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
    }

  },
  modules: {
  }
}
