<template>
  <div>
    <h2>Choose Movie View</h2>
    <p>연인과의 시간을 가지고 싶다면</p>
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
  name: 'LoverMovieView',
  components: {
    ChooseItem,
    ChooseMovieItem
  },
  data() {
    return {
      movies: null,
      genreList: [10749, 27, 10402, 35],
      radomMovies: null,
    }
  },
  created() {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/movies/lovermovie/',
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