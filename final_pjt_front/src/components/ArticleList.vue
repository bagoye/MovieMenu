<template>
  <div class="free-list">

    <ArticleListItem 
      v-for="(article, index) in articles" :key="`article-${index}`"
      :article="article"
    />

  </div>
</template>

<script>
import ArticleListItem from '@/components/ArticleListItem'

export default {
  name: 'ArticleList',
    components: {
    ArticleListItem,
  },
  computed: {
    articles() {
      return this.$store.state.articles
    }
  },
  methods: {

  }
}
</script>

<style>
.free-list {
  width: 95%;
  margin: 0 auto;
}
</style>