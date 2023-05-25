<template>
  <div class="together-list">

    <TogetherListItem 
      v-for="(article, index) in articles" :key="`article-${index}`"
      :article="article"
    />
    
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
.together-list {
  width: 95%;
  margin: 0 auto;
}
</style>