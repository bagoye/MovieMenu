<template>
  <div>
    <!-- 로딩중 빙글빙글 -->
    <div class="spinner-border text-primary" role="status" v-if="movies === null">
      <span class="visually-hidden">Loading...</span>
    </div>


    <span class="movieKeyword" v-if="keyword === 'popular'">인기순</span>
    <span class="movieKeyword" v-else-if="keyword === 'voteaverage'">평점 높은 순</span>
    <span class="movieKeyword" v-else-if="keyword === 'adventure'">모험</span>
    <span class="movieKeyword" v-else-if="keyword === 'action'">액션</span>
    <span class="movieKeyword" v-else-if="keyword === 'sf'">sf</span>
    <NormalMovieListItem
      v-for="(movie, index) in movies" :key="`movie-${index}`"
      :movie="movie"
      class="keywordMovie"
    />
  </div>
</template>

<script>
import NormalMovieListItem from '@/components/NormalMovieListItem'

import axios from 'axios'

export default {
  name: 'NormalMovieList',
  components: {
    NormalMovieListItem,
  },
  props: {
    keyword: String,
  },
  data() {
    return {
      movies: null,
    }
  },
  created() {
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/movies/${this.keyword}/`,
    })
    .then(res => {
      console.log(res)
      this.movies = res.data
    })
    .catch(err => {
      console.log(err)
    })
  },

}
</script>

<style>
.keywordMovie {
  border: 2px solid rebeccapurple;
}

.movieKeyword {
  font-size: 24px;
  font-weight: bold;
}
</style>