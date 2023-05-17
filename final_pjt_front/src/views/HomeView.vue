<template>
  <div>
    HOME
    <button @click="toChooseView">로그인한 사람만 누르기 가넝</button>
    <button @click="toMovieView">로그인 안해도 상관 X</button>
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