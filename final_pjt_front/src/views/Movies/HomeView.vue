<template>
  <div class="home-view">
    <div class="menu-out">
      <div class="menu-in">
        <h1 class="h1-tag">오늘의 밥 친구를 찾아서 가보자굿 -0- ;;;;; ;; bb</h1>
        <div>
          <button @click="toChooseView">오늘의 밥친구는 ?! 얘는 로그인 했을 때만 가능</button>
          <button @click="toNormalMovieView">로그인 안해도 상관 X => 개무난한 추천페이지</button>
        </div>
      </div>
    </div>


  </div>
</template>

<script>
export default {
  name: 'HomeView',
  methods: {
 
    toChooseView() {
      this.$router.push({name: 'ChooseView'})
    },
    toNormalMovieView() {
      this.$router.push({name: 'NormalMovieView'})
    }
    },
  }

</script>

<style>
.home-view {
  width: 100%;
  text-align: center;
}

.menu-out {
  width: 100%;
  height: 500px;
  background-color: #D6E7F6;
  border-radius: 20px 20px 0 0;
  position: relative;
}
.menu-in {
  width: 90%;
  height: 90%;
  position: absolute;
  left: 5%;
  bottom: 0;
  border-radius: 20px 20px 0 0;
  background-color: #fff;
}
</style>