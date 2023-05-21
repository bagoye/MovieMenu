import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  state: {
    articles: [],
  },
  getters: {
    articles: (state) => state.articles,
  },
  mutations: {
    GET_ARTICLES(state, articles) {
      state.articles = articles
    }
  },
  actions: {
    getArticles(context) {
      axios({
        method: 'get',
        url: `${API_URL}/community/free/`,
        headers: context.getters.authHeader
      })
        .then((res) => {
        // console.log(res, context)
          context.commit('GET_ARTICLES', res.data)
        })
        .catch((err) => {
          console.log(err)          
        })
    }
  },
}
