<template>
  <div class="choose-view">
    <div class="menu-out">
      <div class="menu-in">
        <h1 class="mt-5">오늘 나와 함께 할 사람은?</h1>

        <div class="mt-2">
          <button @click="toAloneMovieView" class="btn-com1 btn-hover">혼자만의 시간을 갖고 싶어요!</button>
          <button @click="toLoverMovieView" class="btn-com1 btn-hover">연인과 함께 시간을 보낼래요!</button>
          <button @click="toFriendMovieView" class="btn-com1 btn-hover">친구와 함께 시간을 보낼래요!</button>
          <button @click="toFamilyMovieView" class="btn-com1 btn-hover">가족과 함께 시간을 보낼래요!</button>
        </div>
      </div>
    </div>
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
    },
    toFriendMovieView() {
      this.$router.push({name: 'FriendMovieView'})
    },
    toFamilyMovieView() {
      this.$router.push({name: 'FamilyMovieView'})
    },
  }
}
</script>

<style>
.choose-view {
  width: 100%;
  text-align: center;
}

.btn-hover:hover {
  background-color: #2E8ADF;
  color: #fff;
}
</style>