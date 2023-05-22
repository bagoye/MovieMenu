<template>
  <div>
    TogetherList
    <TogetherListItem 
      v-for="(article, index) in articles" :key="`article-${index}`"
      :article="article"
    />
    <!-- <ArticleListItem /> -->
  </div>
</template>

<script>
import TogetherListItem from '@/components/TogetherListItem'

export default {
  name: 'TogetherList',
    components: {
    TogetherListItem,
  },
  computed: {
    articles() {
      return this.$store.state.articlesTogether
    }
  },
  methods: {

  }
}
</script>

<style>

</style>