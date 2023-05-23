<template>
  <div>
    <h1>같이봐욥 게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title"><br>
      <label for="content">내용 : </label>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
      <input type="submit" id="submit">

    </form>

    <form @submit.prevent="searchMovie">
      <label for="search">영화 검색 : </label>
      <input type="text" name="search" id="search" v-model="search">
      <input type="submit" name="search" id="search" value="제출">
    </form>
    
    <ul>
      <li v-for="result in searchResult" :key="result.id" @click="toResultMovie(result)">{{ result.title }}</li>
    </ul>
    
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
import { mapGetters, mapActions } from 'vuex'
export default {
  name: 'TogetherCreateView',
  data() {
    return {
      title: null,
      content: null,

      movies: null,
      search: null,
      searchResult: [],
      resultMovie: null,
    }
  },
  computed: {
    ...mapGetters(['selectMovie'])
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
    createArticle() {
      const title = this.title
      const content = this.content
      const article = {
        title: this.title,
        content: this.content,
        movie_id: this.selectMovie.id // 영화 정보를 게시글에 추가
      };

      if (!title) {
        alert('제목 입력해주세요')
        return
      } else if (!content){
        alert('내용 입력해주세요')
        return
      }

      axios({
        method: 'post',
        url: `${API_URL}/community/together/`,
        // data: { title, content},
        data: article,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        // this.$router.push({name: 'TogetherCommunityView'})
        const article = res.data;
        article.searchResult = this.searchResult;
        this.$store.commit('ADD_ARTICLE_TOGETHER', article); // Vuex에 게시글 추가
        this.$router.push({ name: 'TogetherCommunityView' });
        console.log(article.id)
        console.log(article, '==========================')
      })
      .catch((err) => {
        console.log(err)
        console.log('같이봐욥 post에서 오류 발생')
      })
    },
    searchMovie() {
      if (this.movies && this.search) {
        this.searchResult = this.movies.filter((movie) =>
          movie.title.includes(this.search)
        );
      } else {
        this.searchResult = [];
      }
    },
    ...mapActions(['setResultMovie']),
    toResultMovie(movie) {
      this.setResultMovie(movie)
      console.log(this.getResultMovie) // Vuex store의 resultMovie 데이터 확인
    }

  }
}
</script>

<style>

</style>