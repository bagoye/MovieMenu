
import axios from 'axios'
import router from '@/router'
const API_URL = 'http://127.0.0.1:8000'


export default {
  state: {
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
      router.push({name : 'HomeView'}).catch(() => {})
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
    }

  },
  modules: {
  }
}
