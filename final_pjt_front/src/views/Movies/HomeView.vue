<template>
  <div class="home-view">
    <div class="menu-out">
      <div class="menu-in">
        <h1 class="mt-5">오늘의 밥 친구를 추천해드릴게요!</h1>
        <div>
          <button @click="toChooseView" class="btn-com1 btn-blue">오늘의 밥 친구를 추천 받을래요!</button>
          <button @click="toNormalMovieView" class="btn-com1">카테고리별 추천을 받고 싶어요!</button>
        </div>
      </div>
    </div>


  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'HomeView',
  computed: {
    ...mapGetters(['isLogin'])
  },
  methods: {
 
    toChooseView() {
      if (this.isLogin) {
        this.$router.push({name: 'ChooseView'})
      } else if (!this.isLogin) {
        this.$router.push({name: 'LoginView'})
      }
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
  min-height: calc(100vh - 150px);
  background-color: #D6E7F6;
  border-radius: 20px 20px 0 0;
  position: relative;
}
.menu-in {
  width: 90%;
  height: calc(100% - 50px);
  position: absolute;
  left: 5%;
  top: 50px;
  border-radius: 20px 20px 0 0;
  background-color: #fff;
}

.btn-com1 {
  width: 72%;
  height: 48px;
  border-radius: 10px;
  border: none;
  margin-top: 10px;
  font-size: 16px;
}
.btn-blue {
  background-color: #2E8ADF;
  color: #fff;  
}

button:hover {
  font-weight: bold;
}
</style>