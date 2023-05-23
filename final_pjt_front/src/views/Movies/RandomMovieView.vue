<template>
  <div class="random-movie">
    <div class="menu-out">
      <div class="menu-in">
        <h1 class="mt-5">오늘의 추천 메뉴</h1>
        <div>
          <div @click="pickOneMovie" class="cardbox">
            <img v-if="pickOne" :src="`https://image.tmdb.org/t/p/w300_and_h450_bestv2${pickOne.poster_path}`" class="card-img-top" alt="...">
            <div class="card-body">
              <h5 class="card-title">{{ pickOne.title }}</h5>
            </div>
          </div>
          <span>클릭해주세요</span>
        </div>
        <div>
          <h2>영화 제목</h2>
          <span>영화 설명해주는 것 100자로 해두고?! 이제 암튼... 오켕이</span>
          <div>
            <button>이 영화로 할게요</button>
            <button @click="pickOneMovie">다시 뽑을래요</button>
          </div>
          <div>
            <span>나의 취향과 상황에 맞춰 추천을 받고 싶다면?</span>
            <button>선택하러 가기</button>
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
    })
    .catch(err => {
      console.log(err)
    })
  },
  methods: {
    pickOneMovie() {
      this.pickOne = _.sample(this.movies)
    }
  }
}

</script>

<style>
.cardbox {
  width: 400px;
  height: 600px;
  background-color: #ccc;
}

</style>