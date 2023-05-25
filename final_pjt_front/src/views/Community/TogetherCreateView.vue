<template>
  <div class="together-create">
    <h1>영화 같이 봐요 <span class="text-blue">작성하기</span></h1>

    <div class="together-create-wrap row">
      <div class="article-form col-sm-12 col-lg-6">
        <form @submit.prevent="createArticle">
          <div>
            <label for="title"><b>제목</b></label><br>
            <input type="text" class="mt-2" id="title" v-model.trim="title" placeholder="제목을 작성해주세요!"><br>
          </div>
          <div>
            <label for="content" class="mt-4"><b>내용</b></label><br>
            <textarea id="content" class="mt-2" cols="30" rows="10" v-model="content" placeholder="내용을 작성해주세요!"></textarea><br>
          </div>
          <input type="submit" id="submit" class="my-4 btn-blue submit-btn">
        </form>
      </div>

      <div class="search-form col-sm-12 col-lg-6">
        <!-- 영화 검색 폼 -->
        <form @submit.prevent="searchMovie">
          <label for="search"><b>영화 검색</b></label><br>
          <input type="text" name="search" id="search" v-model="search" class="mt-2">
          <input type="submit" name="search" id="search" value="검색" class="my-4 search-btn">
        </form>
        <!-- 영화 검색 결과가 나오는 곳 -->
        <ul class="search-movies" v-if="searchResult.length > 0">
          <li v-for="result in searchResult" :key="result.id" @click="toResultMovie(result)">{{ result.title }}</li>
        </ul>
      </div>
    </div>
    
    
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
      } else if (!this.search) {
        alert('영화를 검색하고 선택해주세요!')
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
.together-create-wrap {
  margin-top: 50px;
  text-align: center;
}

.article-form input, .article-form textarea, .search-form input {
  width: 70%;
  border-radius: 5px;
  border: 1px solid #2E8ADF;
}

.search-form ul {
  width: 70%;
  
  margin: 0 auto;
  padding: 0;
  border-radius: 5px;
  overflow: hidden;
  border: 1px solid #2E8ADF;
}
.search-form li {
  width: 100%;
  padding: 5px;
}

.search-form li:nth-child(2n) {
  background-color: #D6E7F6;
}

.search-btn {
  background-color: #fff;
  color: #2E8ADF;
}

.search-btn:hover, .submit-btn:hover {
  font-weight: bold;
}
</style>