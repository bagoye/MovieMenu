<template>
  <div class="movie-detail">
    <h1 class="movieKeyword">{{ movie?.title }}</h1>
    <iframe width="100%" height="400px" :src="`https://www.youtube.com/embed/${movie?.youtube_key}`" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    
    <div class="detail-middle mt-3">
      <button class="like-btn" @click="toggleLike" :class="{ liked: isLiked }">
        {{ isLiked ? '좋아요 취소' : '좋아요' }}
      </button>
      <div class="d-flex">
        <p class="mx-5"><b>평점 : </b>{{ movie?.vote_average }} 점</p>
        <p class="mx-1"><b>러닝 타임 : </b>{{ formatRuntime(movie?.runtime) }}</p>
      </div>
    </div>

    <div class="crew d-flex row">

      <div class="director mt-5 col-sm-12 col-lg-3">
        <span><b>감독</b></span>
        <div class="crew-img mt-3">
          <img :src="`https://image.tmdb.org/t/p/w300_and_h450_bestv2${movie?.directors[0].profile_path}`" @error="handleImageErrorDirector">
        </div>
        <div class="crew-name">{{ movie?.directors[0].name }}</div>
      </div>

      <div class="actor mt-5 col-sm-12 col-lg-9">
        <span><b>배우</b></span>
        <div class="d-flex justify-content-between mt-3 mx-1">
          <div v-for="(actor, index) in movie?.actors" :key="index" class="actor-wrap">
            <div class="crew-img actor-img">
              <img :src="`https://image.tmdb.org/t/p/w300_and_h450_bestv2${actor.profile_path}`" @error="handleImageErrorActor">
            </div>
            <div class="crew-name actor-name">{{ actor.name }}</div>
          </div>
        </div>
      </div>

    </div>

    <div class="overview">
      <div><b>줄거리</b></div>
      <div class="mt-3">{{ movie?.overview }}</div>
    </div>

    <div class="review-list my-5">
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

    // 이미지 오류가 생겼을 때, 대체 이미지로 변경
    handleImageErrorDirector(event) {
      event.target.src = require('@/assets/director.png')
    },
    handleImageErrorActor(event) {
      event.target.src = require('@/assets/actor.png')
    },
    formatRuntime(minutes) {
      const hours = Math.floor(minutes / 60);
      const mins = minutes % 60;
      return `${hours}H ${mins}M`;
    },
  },
}
</script>

<style>
/* 좋아요 */
.like-btn {
  width: 150px;
  height: 44px;
  background-color: #fff;
  border: 1px solid #2E8ADF;
  color: #2E8ADF;;
  border-radius: 5px;
}
.liked {
  background-color: #2E8ADF;
  color: #fff;
  font-weight: bold;
}

/* 동영상 테두리 둥글게 */
iframe { 
  border-radius: 10px;
  margin-top: 20px;
}

.crew-img {
  width: 100px;
  height: 100px;
  border-radius: 10px;
  overflow: hidden;
  background-color: #D6E7F6;
}
.crew-img > img {
  width: 100px;
  height: 100px;
  object-fit: cover;
}


.detail-middle {
  width: 100%;
  height: 44px;
  line-height: 44px;
  display: flex;
  justify-content: space-between;
}
.detail-middle button {
  line-height: 0;
}

.crew-name {
  margin-top: 10px;
}

.actor-wrap {
  position: relative;
}
.actor-name {
  margin-top: 5px;
  opacity: 0;
  width: 100px;
  padding: 5px;
  border-radius: 5px;
  background-color: #D6E7F6;
  text-align: center;
  position: absolute;
  top: 110px;
  transition: 0.5s;
}

.actor-name:after {
  content : '';  
  position: absolute;       
  background-color:#D6E7F6;
  width : 10px;
  height: 10px;
  transform: rotate(45deg) translateX(-50%);
  top: 0;
  left: 50%;                                  
}

.actor-wrap:hover .actor-name {
  opacity: 1;
}

.overview {
  margin-top: 80px;
}

</style>