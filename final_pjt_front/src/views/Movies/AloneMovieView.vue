<template>
  <div class="alone-movie">
    <h2 class="movieKeyword my-5">혼자만의 시간<span class="light-font">을 가지고 싶다면,</span></h2>
    <div class="genre-lst row">
      <div class="col-sm-6 col-lg-3">드라마</div>
      <div class="col-sm-6 col-lg-3">미스터리</div>
      <div class="col-sm-6 col-lg-3">코미디</div>
      <div class="col-sm-6 col-lg-3">판타지</div>
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
  name: 'AloneMovieView',
  components: {
    ChooseMovieItem
  },
  data() {
    return {
      movies: null,
      genreList: [18, 9648, 14, 35],
      radomMovies: null,
    }
  },
  created() {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/movies/alonemovie/',
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
.genre-lst {
  border-radius: 5px;
  overflow: hidden;
  border: 1px solid #2E8ADF;
}
.genre-lst div:nth-child(2n) {
  background-color: #fff;
  color: #2E8ADF;
}
.genre-lst > div {
  height: 44px;
  line-height: 44px;
  text-align: center;
  background-color: #2E8ADF;
  color: #fff;
}

.want-back {
  color: #2E8ADF;
  text-align: center;
  cursor: pointer;
}
.alone-movie {
  width: 100%;
}
.alone-movie button {
  width: 60%;
  height: 44px;
  border: none;
  background-color: #2E8ADF;
  color: #fff;
  border-radius: 10px;
}
</style>

<!-- 
data() {
  return {
    person: '',
    genreList: [],
  };
},
mounted() {
  this.person = this.$route.params.person;
},
created() {
  if (this.person === 'alone') {
    // 드라마, 미스터리, 판타지, 코미디
    this.genreList = [18, 9648, 14, 35]
  } else if (this.person === 'friend') {
    // 액션, 범죄, 스릴러, SF
    this.genreList = [28, 80, 53, 878]
  } else if (this.person === 'lover') {
    // 로맨스, 공포, 음악, 코미디
    this.genreList = [10749, 27, 10402, 35]
  } else if (this.person === 'family') {
    // 애니메이션, 가족, 드라마, 모험
    this.genreList = [16, 10751, 18, 12]
  }
},
methods: {
  toChooseView() {
    this.$router.push({name: 'ChooseView'})
  },
}, -->