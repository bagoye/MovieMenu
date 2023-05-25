<template>
  <div class="free-list-item">

    <div class="article-item row">
      <p class="col-1"><b>{{ article.id }}</b></p>
      <router-link :to="{
        name: 'FreeDetailView',
        params: {freepk: article.id}}"
        class="col-6">
        {{ article.title }}
      </router-link>
      <p class="col-3">{{ article.created_at | formatDate }}</p>
      <router-link :to="{
        name: 'FreeDetailView',
        params: {freepk: article.id}}"
        class="col-2">
        [자세히]
      </router-link>
    </div>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'ArticleListItem',
  props: {
    article: Object,
  },
  filters: {
    formatDate(value) {
    const date = new Date(value);
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
    },
  },
}
</script>

<style>
.article-item {
  text-align: center;
}
</style>
