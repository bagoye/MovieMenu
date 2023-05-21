import Vue from 'vue'
import Vuex from 'vuex'

import createPersistedState from 'vuex-persistedstate'

import accounts from './modules/accounts'
import community from './modules/community'


Vue.use(Vuex)


export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  
  modules: {
    accounts,
    community,
  }
})
