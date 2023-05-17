<template>
  <div>
    {{ 혼자, 애인, 가족, 친구 }} v-if로 잘 넣어주면 될 듯
    상황에 따른 영화 추천
    위에는 일반적인 추천 장르랑, 내가 추가하고 뺄 수 있도록 버튼으로 만들거임
    호버로 추가 빼기 가능
    밑에는 ChooseMovieList.vue 가져와서 보여주기
    우선은 8개정도만 보여주고 새로고침 혹은 인피니티 스크롤 ,,?
    <div>
      <div class='chooseBox' @click="changeGenre">
        1
      </div>
      <div class='chooseBox'>
        2
      </div>
      <div class='chooseBox'>
        3
      </div>
      <div class='chooseBox'>
        4
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ChooseMovieView',
  methods: {
    changeGenre() {
      
    }
  }
}
</script>

<style>

</style>