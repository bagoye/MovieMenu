<template>
  <div>
    ArticleList
    <ArticleListItem 
      v-for="(article, index) in articles" :key="`article-${index}`"
      :article="article"
    />
    <!-- <ArticleListItem /> -->
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

</style>