<template>
  <div>
    FreeCommunityView
    <span v-if="isLogin">
      <router-link :to="{name : 'FreeCreateView'}">[CREATE]</router-link>
    </span>
    <ArticleList/>
    

  </div>
</template>

<script>
import ArticleList from '@/components/ArticleList'
import { mapGetters } from 'vuex'

export default {
  name: 'FreeCommunityView',
  components: {
    ArticleList,
  },
  computed: {
    ...mapGetters(['isLogin']),
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles() {
      this.$store.dispatch('getArticles')
    }
  }
}
</script>

<style>

</style>