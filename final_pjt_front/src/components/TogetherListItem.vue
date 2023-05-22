<template>
  <div>
    <h1>{{ article.id }}</h1>
    <p>{{ article.title }}</p>
    <router-link :to="{
      name: 'TogetherDetailView',
      params: {togetherpk: article.id}}">
      [DETAIL]
    </router-link>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'TogetherListItem',
  props: {
    article: Object,
  }
}
</script>

<style>

</style>
