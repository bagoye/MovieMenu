<template>
  <div>
    <h1>영화를 함께 할 사람은 ?!!?</h1>

    <div>
      <button @click="toAloneMovieView">혼자</button>
      <button @click="toLoverMovieView">연인과</button>
      <button >친구들과</button>
      <button >가족들과</button>
    </div>
      선택하면 선택한 테마의 영화 추천 페이지 (ChooseMovieView) 로 넘어감
      
  </div>
</template>

<script>
export default {
  name: 'ChooseView',
  methods: {
    toAloneMovieView() {
      this.$router.push({name: 'AloneMovieView'})
    },
    toLoverMovieView() {
      this.$router.push({name: 'LoverMovieView'})
    }
  }
}
</script>

<style>

</style>



<!-- <template>
  <div>
    <h1>영화를 함께 할 사람은 ?!!?</h1>

    <div>
      <button @click="toChooseMovieView('alone')">혼자</button>
      <button @click="toChooseMovieView('lover')">연인과</button>
      <button @click="toChooseMovieView('friend')">친구들과</button>
      <button @click="toChooseMovieView('family')">가족들과</button>
    </div>
      선택하면 선택한 테마의 영화 추천 페이지 (ChooseMovieView) 로 넘어감
      
  </div>
</template>

<script>
export default {
  name: 'ChooseView',
  methods: {
    toChooseMovieView(person) {
      this.$router.push({
        name: 'ChooseMovieView',
        params: {
          person: person
        }
      })
    }
  }
}
</script>

<style>

</style> -->

