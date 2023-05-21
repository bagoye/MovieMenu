<template>
  <div>
    ArticleList
    <ArticleListItem 
    v-for="article in articles" :key="article.id" :article="article"/>
  </div>
</template>

<script>
import ArticleListItem from '@/components/ArticleListItem'
import { mapGetters } from 'vuex'
export default {
  name: 'ArticleList',
    components: {
    ArticleListItem,
  },
  computed: {
    ...mapGetters(['articles', ]),
  }
}
</script>

<style>

</style>