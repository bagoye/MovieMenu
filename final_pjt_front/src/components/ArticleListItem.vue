<template>
  <div>
    <h1>{{ article.id }}</h1>
    <p>{{ article.title }}</p>
    <router-link :to="{
      name: 'FreeDetailView',
      params: {freepk: article.id}}">
      [DETAIL]
    </router-link>
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
