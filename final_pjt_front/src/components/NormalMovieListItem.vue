<template>
  <div class="col-sm-6 col-md-4 col-lg-2">
    <div class="movie-card">
      <img :src="`https://image.tmdb.org/t/p/w300_and_h450_bestv2${movie.poster_path}`">

      <div class="movie-trans"></div>

      <div class="movie-card-content">
        <div class="movie-title">{{ movie.title }}</div>
        <div class="movie-title">{{ formatRuntime(movie.runtime) }}</div>
        <div class="movie-btn">
          <router-link
            :to="{
              name:'MovieDetailView', 
              params: { pk: movie.id }}">
            <button>▶</button>
          </router-link>
          <button @click="toggleLike" :class="{ liked: isLiked }">
            {{ isLiked ? '✅' : '😍' }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'NormalMovieListItem',
  props: {
    movie: Object,
    userId: String,
  },
  data() {
    return {
      isLiked: false, // 버튼 상태를 저장하는 데이터 속성 추가
    };
  },
  created() {
    this.isLiked = this.checkIsLiked(); // 페이지 로드 시 좋아요 상태 초기화
  },
  methods: {
    formatRuntime(minutes) {
      const hours = Math.floor(minutes / 60);
      const mins = minutes % 60;
      return `${hours}H ${mins}M`;
    },
    toggleLike() {
      const userLikesKey = `userLikes:${this.$store.state.userInfo.pk}`;
      const userLikes = JSON.parse(localStorage.getItem(userLikesKey)) || {};

      if (userLikes[this.movie.id]) {
        delete userLikes[this.movie.id];
        this.isLiked = false; // 버튼 상태 변경
      } else {
        userLikes[this.movie.id] = true;
        this.isLiked = true; // 버튼 상태 변경
      }

      localStorage.setItem(userLikesKey, JSON.stringify(userLikes));
      this.$emit('like-updated', userLikes); // 좋아요 상태 변경을 부모 컴포넌트로 알림
    },
    checkIsLiked() {
      const userLikesKey = `userLikes:${this.userId}`;
      const userLikes = JSON.parse(localStorage.getItem(userLikesKey)) || {};
      return !!userLikes[this.movie.id];
    },
  },
};
</script>

<style scoped>

.movie-card {
  position: relative;
  text-align: center;
  border-radius: 10px;
  overflow: hidden;
}

.movie-card img {
  width: 100%;
}

.movie-card-content {
  width: 100%;
  position: absolute;
  top: 20%;
  color: #fff;
  text-align: center;
  display: flex;
  flex-direction: column;
  visibility: hidden;
  transition: opacity 0.3s ease;
}

.movie-trans {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: #000;
  opacity: 60%;
  visibility: hidden;
}

.movie-card-content * {
  margin: 10% 0;
}
.movie-card:hover .movie-card-content {
  visibility: visible;
}
.movie-card:hover .movie-trans {
  visibility: visible;
}

.movie-btn * {
  /* margin: 0 20px; */
  width: 36px;
  height: 36px;
  border: none;
  border-radius: 50%;
}
.movie-btn button {
  margin: 0 20px;
}

</style>