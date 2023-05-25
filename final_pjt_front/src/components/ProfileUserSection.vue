<template> 
  <div class="profile-user-section">
    <h1 class="profile-title">{{ user.username }}님의 마이페이지</h1>
    <hr>

    <div>
      <div class="user-articles row">
        <h1>{{ user.username }}님이 <span class="text-blue">작성한 글</span></h1>
        
        <div class="free-articles col-sm-12 col-lg-6">
          <div class="profile-article mb-3">자유 게시판</div>
          <div v-for="freearticle in userarticles" :key="freearticle.id" class="hr-none">
            <router-link
            :to="{
              name:'FreeDetailView', 
              params: { freepk: freearticle.id }}">
              제목 : {{ freearticle.title }}
            </router-link>
            <span style="margin-left:20px;">
              내용 : {{ freearticle.content }}
            </span>
            <hr>
          </div>
        </div>

        <div class="together-articles col-sm-12 col-lg-6">
          <div class="profile-article mb-3">영화 같이 봐요</div>
            <div v-for="togetherarticle in togetherarticles" :key="togetherarticle.id" class="hr-none">
              <router-link :to="{ name: 'TogetherDetailView', params: { togetherpk: togetherarticle.id }}">
                제목 : {{ togetherarticle.title }}
              </router-link>
              <span style="margin-left:20px;">
                내용: {{ togetherarticle.content }}
              </span>
              <hr>
            </div>
          </div>
        </div>
      </div>
    <hr>
    <h1>{{ user.username }}님이 <span class="text-blue">좋아하는 영화</span></h1>
      <div v-if="movies.length > 0" class="row mt-4">
        <div v-for="movie in movies" :key="movie.id" class="col-sm-6 col-lg-4 like-movie-wrap">
          <div class="like-movie-img">
            <router-link
              :to="{
                name:'MovieDetailView', 
                params: { pk: movie.pk }}">
            <img :src="`https://image.tmdb.org/t/p/w300_and_h450_bestv2${movie.poster_path}`">
            </router-link>
          </div>
          <div class="like-movie-title">{{ movie.title }}</div>
          
        </div> 
      </div>

      <div v-else class="my-5 text-center">
        <p>좋아하는 영화가 없습니다.</p>
      </div>
    <hr>
    <h1>{{ user.username }}님이 <span class="text-blue">작성한 리뷰</span></h1>
      <div v-for="(review,index) in userReviews" :key="index" class="hr-none user-review">
        <span class="text-blue">{{ review.user.username }}님</span>
        <span>{{ review.content }}</span>
        <hr>
      </div>

  </div>
</template>

<script>

import axios from 'axios'

export default {
  name: 'ProfileUserSection',
  data() {
    return {
      user: this.$store.state.userInfo,
      userarticles: null,
      togetherarticles: [],
      movies: [],
      userReviews: [],
    }
  },
  computed: {
    articles() {
      return this.$store.state.articles;
    },
    articlesTogether() {
      return this.$store.state.articlesTogether
    },
    likedMovies() {
      const userLikesKey = `userLikes:${this.user.pk}`;
      const userLikes = JSON.parse(localStorage.getItem(userLikesKey)) || {};
      return Object.keys(userLikes).filter((movieId) => userLikes[movieId]);
    },
  },
  created() {
    this.findUserArticle();
    this.findUserTogetherArticle();

    const userLikesKey = `userLikes:${this.user.pk}`;
    const userLikes = JSON.parse(localStorage.getItem(userLikesKey)) || {};

    const movieIds = Object.keys(userLikes).filter((movieId) => userLikes[movieId]);

    const movieRequests = movieIds.map((movieId) => {
      return axios.get(`http://127.0.0.1:8000/movies/${movieId}/`);
    });

    // 모든 axios 요청을 병렬로 처리하기 위해 Promise.all 사용
    Promise.all(movieRequests)
      .then((responses) => {
        const movies = responses.map((res) => res.data);
        // const moviePoster = responses.map((res) => res.data.poster_path);
        this.movies = movies;
      })
      .catch((error) => {
        console.log(error);
      });

    this.userReviews = this.$store.state.reviews.filter((review) => {
      return review.user.id === this.user.pk;
    });

  },
  
  methods: {
    findUserArticle() {
      const userArticles = this.articles.filter((article) => {
        return article.user === this.$store.state.userInfo.pk;
      });
      this.userarticles = userArticles;
    },
    findUserTogetherArticle() {
      const togetherArticles = this.articlesTogether.filter((article) => {
        return article.user === this.$store.state.userInfo.pk;
      });
      this.togetherarticles = togetherArticles;
    },
    getMovieTitle(movieId) {
    // 각 영화에 대한 axios 요청 보내기
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/${movieId}/`
      }) 
      .then((response) => {
        const movieTitle = response.data.title;
        // const moviePoster = response.data.poster_path;
        console.log(movieTitle);
        // return movieTitle, moviePoster;
      })
      .catch(error => {
        console.log(error);
        // 에러 발생 시 대체값 반환 또는 에러 처리 방법 선택
      });
    },
  }
}
</script>

<style>
.profile-user-section {
  width: 85%;
  margin: 0 auto;
}

.profile-user-section hr {
  margin: 40px auto;
}

.profile-title {
  text-align: center;
  font-size: 32px;
  color: #2E8ADF;
}
.text-blue {
  color: #2E8ADF;
}

.profile-article {
  font-size: 20px;
  margin-top: 20px;
}
.free-articles hr, .together-articles hr {
  width: 95%;
  margin: 16px 0;
}

.hr-none:last-child hr {
  display: none;
}

.like-movie-wrap {
  margin: 10px 0;
}
.like-movie-wrap:hover img {
  filter: brightness(50%);
}
.like-movie-img img {
  width: 100%;
  border-radius: 10px;
}

.like-movie-title {
  text-align: center;
  margin-top: 10px; 
}
.user-review {
  margin-top: 40px;
}
.user-review span {
  margin-right: 20px;
}
.user-review hr {
  margin: 20px 0;
}
</style>