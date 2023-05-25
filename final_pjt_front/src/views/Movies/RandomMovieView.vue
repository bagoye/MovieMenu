<template>
  <div class="random-movie">
    <div class="menu-out">
      <div class="menu-in">
        <h1 class="mt-5">오늘의 추천 메뉴</h1>
        <div class="mt-5">
          <div @click="pickOneMovie" class="cardbox">
            <img v-if="pickOne" :src="`https://image.tmdb.org/t/p/w300_and_h450_bestv2${pickOne.poster_path}`" class="card-img-top" alt="...">
            <span v-if="pickOne === ''" class="click-txt">클릭해주세요</span>
          </div>
        </div>

        <div class="right-info">
          <div class="movie-info">
            <h2>{{ pickOne.title }}</h2>
            <div>{{ pickOne.overview }}</div>
            <div>{{ pickOne.runtime }}</div>
          </div>
          <div class="movie-btn">
          <!-- 여기서 클릭해주세요 누르고 영화 정보 나와야 이 영화로 할게요 부분 나오도록 하기 -->
          <router-link
            :to="{
              name:'MovieDetailView', 
              params: { pk: pickOne.id }}">
                <button>
                  이 영화로 할게요
                </button>
          </router-link>
            <!-- <button @click="selectMovie">이 영화로 할게요</button> -->
            <button @click="pickOneMovie">다시 뽑을래요</button>
          </div>
          <div>
            <span>나의 취향과 상황에 맞춰 추천을 받고 싶다면?</span>
            <router-link
              :to="{name:'ChooseView'}">
                <button>
                  선택하러 가기
                </button>
            </router-link>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios'
import _ from 'lodash'

export default {
  name: 'RandomMovieView',
  data() {
    return {
      movies: null,
      pickOne: ''
    }
  },
  created() {
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/movies/allmovie/`,
    })
    .then(res => {
      console.log(res)
      this.movies = res.data
      // this.pickOne = _.sample(this.movies.map(movie => ({ ...movie, liked: false }))) // Add 'liked' property
    })
    .catch(err => {
      console.log(err)
    })
  },
  methods: {
    pickOneMovie() {
      this.pickOne = _.sample(this.movies.map(movie => ({ ...movie, liked: false }))) // Reset 'liked' property
    },
  }
}

</script>

<style>
.random-movie {
  text-align: center;
}

.cardbox {
  cursor: pointer;
  width: 300px;
  margin: 0 auto;
  height: 450px;
  border-radius: 10px;
  background-color: #D6E7F6;

  overflow: hidden;
}

.cardbox:hover {
  background-color: #c0dbf3;
}

.click-txt {
  line-height: 450px;
}

</style>