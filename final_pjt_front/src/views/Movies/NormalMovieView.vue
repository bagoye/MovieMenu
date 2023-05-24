<template>
  <div class="normal-movie-view">
    <div class="normal-banner">
      <div class="banner-img"></div>
      <div class="banner-trans"></div>
      <div class="banner-info">
        <div>더 많은 영화를 내 취향과 상황에 맞추고 싶다면,</div>
        <button class="btn-com2 btn-blue mt-5">추천 받으러 가기</button>
      </div>
    </div>

    <NormalMovieList
      v-for="(keyword, index) in keywords" :key="`keyword-${index}`"
      :keyword="keyword"
    />

    <div class="go-top" onClick="javascript:window.scrollTo(0,0)">TOP</div>
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
}
.banner-img {
  width: 100%;
  height: 100%;
  background: url(@/assets/cats.jpg) no-repeat center center fixed;

}

.banner-info {
  width: 100%;
  text-align: center;
  top: 200px;
  position: absolute;
}
.banner-info > div {
  font-size: 24px;
}

.btn-com2 {
  width: 307px;
  height: 48px;
  border-radius: 10px;
  border: none;
  margin-top: 10px;
  font-size: 16px;
}

/* 투명도 70% */
.banner-trans {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  
  background-color: #fff;
  opacity: 50%;
}

/* 상단으로 이동하기 */
.go-top {
  width: 60px;
  height: 60px;
  background-color: #2E8ADF;
  border-radius: 10px;
  position: fixed;
  bottom: 20px;
  right: 20px;
  cursor: pointer;

  text-align: center;
  line-height: 60px;
  color: #fff;
  font-size: 16px;
  font-weight: bold;
}
</style>