<template>
  <div class="choose-item">
    <router-link class="item-link"
    :to="{
      name:'MovieDetailView', 
      params: { pk: movie.id }}">
      <img :src="`https://image.tmdb.org/t/p/w300_and_h450_bestv2${movie.poster_path}`">
      <div class="movie-info-wrap">
        <div>{{ movie.title }}</div>
        <div>{{ formatRuntime(movie.runtime) }}</div>
        <div>영화 세부 내용 보기</div>
      </div>
    </router-link>
    

  </div>
</template>

<script>
export default {
  name: 'ChooseMovieItem',
  props: {
    movie: Object
  },
  methods: {
    formatRuntime(minutes) {
      const hours = Math.floor(minutes / 60);
      const mins = minutes % 60;
      return `${hours}H ${mins}M`;
    },
  }

}
</script>

<style>
.choose-item img {
  width: 100%;
  border-radius: 10px;
}
.choose-item>.item-link:hover img {
  filter: brightness(45%);
}

.choose-item {
  margin-bottom: 20px;
}

.item-link {
  position: relative;
}

.movie-info-wrap {
  width: 100%;
  top: -55px;
  position: absolute;
  text-align: center;
  visibility: hidden;
  color: #fff;
}
.movie-info-wrap > * {
  margin: 20px 0;
}

.choose-item:hover .movie-info-wrap {
  visibility: visible;
}
.choose-item:hover .choose-trans {
  visibility: visible;
}
</style>