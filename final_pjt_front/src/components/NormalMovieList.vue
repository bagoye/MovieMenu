<template>
  <div>
    <span class="movieKeyword" v-if="keyword === 'popular'">인기순</span>
    <span class="movieKeyword" v-else-if="keyword === 'upcoming'">개봉 예정작</span>
    <span class="movieKeyword" v-else>높은 평점순</span>
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
      url: `https://api.themoviedb.org/3/movie/${this.keyword}/`,
      params: {
        api_key: "779716af9004289d5cc205ea82476fab",
        language: "ko-KR",
      },
    })
    .then(res => {
      console.log(res)
      this.movies = res.data.results
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