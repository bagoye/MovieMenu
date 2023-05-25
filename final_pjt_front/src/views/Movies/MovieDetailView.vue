<template>
  <div class="movie-detail">
    <h1 class="movieKeyword">{{ movie?.title }}</h1>
    <iframe width="100%" height="400px" :src="`https://www.youtube.com/embed/${movie?.youtube_key}`" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    
    <p>평점 : {{ movie?.vote_average }}</p>
    <p>러닝타임 : {{ movie?.runtime }}</p>
    <p>감독 : 
      <img :src="`https://image.tmdb.org/t/p/w300_and_h450_bestv2${movie?.directors[0].profile_path}`" style="width: 100px;">
      {{ movie?.directors[0].name }}
    </p>
    <!-- <p>배우 : {{ movie?.actors }}</p> -->
    <p>배우:</p>
      <div v-for="(actor, index) in movie?.actors" :key="index">
        <img :src="`https://image.tmdb.org/t/p/w300_and_h450_bestv2${actor.profile_path}`" style="width: 100px;">
        {{ actor.name }}
      </div>
    <p>줄거리: {{ movie?.overview }} </p>
    <button @click="toggleLike" :class="{ liked: isLiked }">
      {{ isLiked ? '✅' : '😍' }}
    </button>

    <div class="review-list">
      <ReviewList />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ReviewList from '@/components/ReviewList'

export default {
  name: 'MovieDetailView',
  components: {
    ReviewList,
  },
  data() {
    return {
      movie: null,
      isLiked: false,
    }
  },
  async created() {
    await this.getMovieDetail();
    window.scrollTo(0, 0); // 스크롤 위치 조정
    this.checkIsLiked();
  },
  // mounted() {
  //   this.checkIsLiked();
  // },
  methods: {
    getMovieDetail() {
      return axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/${this.$route.params.pk}/`
      })
      .then((res) => {
        console.log(res.data)
        this.movie = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    toggleLike() {
      const userLikesKey = `userLikes:${this.$store.state.userInfo.pk}`;
      const userLikes = JSON.parse(localStorage.getItem(userLikesKey)) || {};

      if (userLikes[this.movie.pk]) {
        delete userLikes[this.movie.pk];
        this.isLiked = false; // 버튼 상태 변경
      } else {
        userLikes[this.movie.pk] = true;
        this.isLiked = true; // 버튼 상태 변경
      }

      localStorage.setItem(userLikesKey, JSON.stringify(userLikes));
      this.$emit('like-updated', userLikes); // 좋아요 상태 변경을 부모 컴포넌트로 알림
    },
    async checkIsLiked() {
      await this.getMovieDetail(); // `getMovieDetail` 메소드 완료 대기
      const userLikesKey = `userLikes:${this.$store.state.userInfo.pk}`;
      const userLikes = JSON.parse(localStorage.getItem(userLikesKey)) || {};
      this.isLiked = !!userLikes[this.movie.pk];
    },
  },
}
</script>

<style>
.liked {
  color: red;
  font-weight: bold;
}
</style>