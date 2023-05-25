<template>
  <div class="normal-list row">

    <div class="normal-content mt-5 mx-auto col-10">
      <div class="movieKeyword" v-if="keyword === 'popular'">인기순 <span class="light-font">모아보기</span></div>
      <div class="movieKeyword" v-else-if="keyword === 'voteaverage'">평점순 <span class="light-font">모아보기</span></div>
      <div class="movieKeyword" v-else-if="keyword === 'adventure'">모험 <span class="light-font">모아보기</span></div>
      <div class="movieKeyword" v-else-if="keyword === 'action'">액션 <span class="light-font">모아보기</span></div>
      <div class="movieKeyword" v-else-if="keyword === 'sf'">SF <span class="light-font">모아보기</span></div>
    </div>
    <div class="mt-4 col-12 row mx-auto normal-bing">
      <NormalMovieListItem
        v-for="(movie, index) in movies.slice(0, 12)" :key="`movie-${index}`"
        :movie="movie"
      />
      <!-- 로딩중 빙글빙글 -->
      <div class="spinner-border text-primary bingbing" role="status" v-if="movies === null">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>
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
      console.log(res.data)
      this.movies = res.data
    })
    .catch(err => {
      console.log(err)
    })
  },

}
</script>

<style>
.movieKeyword {
  font-size: 32px;
  font-weight: bold;
  color: #2E8ADF;
}

.light-font {
  font-weight: normal;
  color: #000;
}
.normal-bing {
  position: relative;
}
.bingbing {
  position: absolute;
  top: 0;
  left: 50%;
}

</style>