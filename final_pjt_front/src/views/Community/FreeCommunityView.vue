<template>
  <div>
    FreeCommunityView
    <router-link :to="{name : 'FreeCreateView'}">[CREATE]</router-link>
    <ArticleList/>

  </div>
</template>

<script>
import ArticleList from '@/components/ArticleList'
export default {
  name: 'FreeCommunityView',
  components: {
    ArticleList,
  },
  computed:{
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