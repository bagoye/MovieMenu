<template>
  <div>
    <h1>영화를 함께 할 사람은 ?!!?</h1>

    <div>
      <button @click="tochoosemovieview(alibne)">혼자</button>
      <button>연인과</button>
      <button>친구들과</button>
      <button>가족들과</button>
    </div>
      선택하면 선택한 테마의 영화 추천 페이지 (ChooseMovieView) 로 넘어감
      
  </div>
</template>

<script>
export default {
  name: 'ChooseView',
  // methods: {
  //   toChooseMovieView() {
  //     this.$router.push('어쩌구') 먼가 이런식으로 하면 되는걸까 ..? 
  //   }
  // }
}
</script>

<style>

</style>