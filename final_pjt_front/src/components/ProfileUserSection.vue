<template>
  <div>
    ProfileUserSection

    <div>{{ user.pk }}</div>
    <div>{{ user.username }}</div>
    {{ user }} | <br> <hr>

    <p v-for="article in articles" :key="article.id">
      {{ article }}
    </p>

    <br>
    <div>
      <h1>자유게시판</h1>
        <p v-for="userarticle in userarticles" :key="userarticle.id">
        제목:{{ userarticle.title }}  내용:{{ userarticle.content }}
        </p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProfileUserSection',
  data() {
    return {
      user: this.$store.state.userInfo,
      userarticles: null,
    }
  },
  computed: {
    reviews() {
      return this.$store.state.reviews
    },
    articles() {
      return this.$store.state.articles
    },
  },
  created() {
    const movieId = this.$route.params.pk;
    this.$store.dispatch('getReviews', movieId);
    this.findUserArticle()
  },
  methods: {
    findUserArticle() {
      const userArticles = this.articles.filter((article) => {
        return article.user === this.user.pk
      })
      this.userarticles = userArticles
    }
  }
}
</script>

<style>

</style>