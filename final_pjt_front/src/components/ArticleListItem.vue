<template>
  <div>
    <div>안녕하세요아티클리스트아이템</div>
    <h5>{{ article }}</h5>
    <!-- <p>{{ article.title }}</p> -->
    <!-- <router-link :to="{
      name: 'DetailView',
      params: {id: article.id}}">
      [DETAIL]
    </router-link> -->
    <hr>
  </div>
</template>

<script>
export default {
  name: 'ArticleListItem',
  props: {
    article: Object,
  }
}
</script>

<style>

</style>
