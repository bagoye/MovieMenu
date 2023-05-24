<template>
  <div class="normal-movie-view">
    <div class="normal-banner">
      <img src="@/assets/cats.jpg" alt="normal-banner" class="banner-img">
    </div>
    <NormalMovieList
      v-for="(keyword, index) in keywords" :key="`keyword-${index}`"
      :keyword="keyword"
    />
  </div>
</template>

<script>
import NormalMovieList from '@/components/NormalMovieList'

export default {
  name: 'NormalMovieView',
  components: {
    NormalMovieList
  },
  data() {
    return {
      keywords: ['popular', 'voteaverage', 'adventure', 'action' ,'sf']
    }
  },
}
</script>

<style>
.normal-movie-view {
  position: absolute;
  top: 150px;
  width: 100%;
}

.normal-banner {
  width: 100%;
  height: 500px;
  background-color: #D6E7F6;

  position: relative;
  overflow: hidden;

  background-attachment: fixed;
}
.banner-img {
  width: 100%;
  background-size: cover;
  background-position: center;

  
}
</style>