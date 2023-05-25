<template>
  <div class="family-movie">
    <h2 class="movieKeyword my-5">가족과의 시간<span class="light-font">을 가지고 싶다면,</span></h2>
    <div class="genre-lst row">
      <div class="col-sm-6 col-lg-3">애니메이션</div>
      <div class="col-sm-6 col-lg-3">가족</div>
      <div class="col-sm-6 col-lg-3">드라마</div>
      <div class="col-sm-6 col-lg-3">모험</div>
    </div>
    <div class="row mt-5">
    <ChooseMovieItem
    v-for="(movie, index) in radomMovies" :key="`movie-${index}`"
    :movie="movie" class="col-sm-6 col-lg-3"
    />
    </div>

    <div class="text-center mt-3">
      <button @click="randomMovie">더 추천 받고 싶어요!</button>
      <div @click="toChooseView" class="want-back mt-2 mb-5">추천은 괜찮아요, <b>이전으로 돌아갈래요!</b></div>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'
import ChooseMovieItem from '@/components/ChooseMovieItem'

import axios from 'axios'

export default {
  name: 'FamilyMovieView',
  components: {
    ChooseMovieItem
  },
  data() {
    return {
      movies: null,
      genreList: [16, 10751, 18, 12],
      radomMovies: null,
    }
  },
  created() {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/movies/familymovie/',
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

<style>
.family-movie {
  width: 100%;
}
.family-movie button {
  width: 60%;
  height: 44px;
  border: none;
  background-color: #2E8ADF;
  color: #fff;
  border-radius: 10px;
}
</style>