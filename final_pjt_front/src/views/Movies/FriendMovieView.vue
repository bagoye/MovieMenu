<template>
  <div>
    <h2 class="movieKeyword my-5">친구와의 시간<span class="light-font">을 가지고 싶다면,</span></h2>

    <ChooseItem
    v-for="(genre,index) in genreList" :key="`genre-${index}`"
    :genre="genre"
    />
    <ChooseMovieItem
    v-for="(movie, index) in radomMovies" :key="`movie-${index}`"
    :movie="movie"
    />
    <button @click="randomMovie">더 추천받고싶은데욧 -6-;;;;;</button>
    <button @click="toChooseView">이전페이지</button>
  </div>
</template>

<script>
import _ from 'lodash'
import ChooseItem from '@/components/ChooseItem'
import ChooseMovieItem from '@/components/ChooseMovieItem'

import axios from 'axios'

export default {
  name: 'FreindMovieView',
  components: {
    ChooseItem,
    ChooseMovieItem
  },
  data() {
    return {
      movies: null,
      genreList: [28, 80, 53, 878],
      radomMovies: null,
    }
  },
  created() {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/movies/friendmovie/',
    })
    .then(res => {
      console.log(res)
      this.movies = res.data
      this.radomMovies = _.sampleSize(this.movies, 8)
    })
    .catch(err => {
      console.log(err)
    })
  },
  methods: {
    toChooseView() {
      this.$router.push({name: 'ChooseView'})
    },
    randomMovie() {
      this.radomMovies = _.sampleSize(this.movies, 8)
    }
  }
}
</script>