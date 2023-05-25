<template>
  <div>
    <h1>{{ user.username }}님의 프로필</h1>
    <hr>
    <div>
      <h1>{{ user.username }}님이 작성한 글</h1>
        <h2>자유게시판</h2>
          <div v-for="freearticle in userarticles" :key="freearticle.id">
            <router-link
            :to="{
              name:'FreeDetailView', 
              params: { freepk: freearticle.id }}">
              {{ freearticle.title }}
            </router-link>
            내용:{{ freearticle.content }}
          </div>

        <h2>같이봐요 게시판</h2>
          <div v-for="togetherarticle in togetherarticles" :key="togetherarticle.id">
            <router-link :to="{ name: 'TogetherDetailView', params: { togetherpk: togetherarticle.id }}">
              {{ togetherarticle.title }}
            </router-link>
            내용: {{ togetherarticle.content }}
          </div>
    </div>
    <hr>
    <h1>좋아하는 영화</h1>
      <div v-if="movies.length > 0">
        <div v-for="movie in movies" :key="movie.id">
          {{ movie.title }}
          <router-link
            :to="{
              name:'MovieDetailView', 
              params: { pk: movie.pk }}">
          <img :src="`https://image.tmdb.org/t/p/w300_and_h450_bestv2${movie.poster_path}`">
          </router-link>
          
        </div> 
      </div>
      <div v-else>
        <p>좋아하는 영화가 없습니다.</p>
      </div>
    <hr>
    <h1>작성한 리뷰</h1>
      <div v-for="review in userReviews" :key="review.id">
        <p>{{ review.content }}</p>
      </div>
  </div>
</template>

<script>

import axios from 'axios'

export default {
  name: 'ProfileUserSection',
  data() {
    return {
      user: this.$store.state.userInfo,
      userarticles: null,
      togetherarticles: [],
      movies: []
    }
  },
  computed: {
    userReviews() {
      return this.$store.state.reviews.filter((review) => {
        return review.user === this.user.pk;
      });
    },
    articles() {
      return this.$store.state.articles;
    },
    likedMovies() {
      const userLikesKey = `userLikes:${this.user.pk}`;
      const userLikes = JSON.parse(localStorage.getItem(userLikesKey)) || {};
      return Object.keys(userLikes).filter((movieId) => userLikes[movieId]);
    },
  },
  created() {
    this.findUserArticle();
    this.findUserTogetherArticle();

    const userLikesKey = `userLikes:${this.user.pk}`;
    const userLikes = JSON.parse(localStorage.getItem(userLikesKey)) || {};

    const movieIds = Object.keys(userLikes).filter((movieId) => userLikes[movieId]);

    const movieRequests = movieIds.map((movieId) => {
      return axios.get(`http://127.0.0.1:8000/movies/${movieId}/`);
    });

    // 모든 axios 요청을 병렬로 처리하기 위해 Promise.all 사용
    Promise.all(movieRequests)
      .then((responses) => {
        const movieTitles = responses.map((res) => res.data);
        // const moviePoster = responses.map((res) => res.data.poster_path);
        this.movies = movieTitles;
      })
      .catch((error) => {
        console.log(error);
      });
  },
  methods: {
    findUserArticle() {
      const userArticles = this.articles.filter((article) => {
        return article.user === this.$store.state.userInfo.pk;
      });
      this.userarticles = userArticles;
    },
    findUserTogetherArticle() {
      const togetherArticles = this.togetherarticles.filter((article) => {
        return article.user === this.$store.state.userInfo.pk;
      });
      this.togetherarticles = togetherArticles;
    },
    getMovieTitle(movieId) {
    // 각 영화에 대한 axios 요청 보내기
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/${movieId}/`
      }) 
      .then((response) => {
        const movieTitle = response.data.title;
        // const moviePoster = response.data.poster_path;
        console.log(movieTitle);
        // return movieTitle, moviePoster;
      })
      .catch(error => {
        console.log(error);
        // 에러 발생 시 대체값 반환 또는 에러 처리 방법 선택
      });
    },
  }
}
</script>

<style>

</style>