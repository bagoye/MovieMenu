<template>
  <div>
    <h1>오늘의 밥 친구를 찾아서 가보자굿 -0- ;;;;; ;; bb</h1>
    <div>
      <button @click="toChooseView">오늘의 밥친구는 ?! 얘는 로그인 했을 때만 가능</button>
      <button @click="toMovieView">로그인 안해도 상관 X => 개무난한 추천페이지</button>
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
    toMovieView() {
      this.$router.push({name: 'MovieView'})
    }
    },
  }

</script>

<style>

</style>