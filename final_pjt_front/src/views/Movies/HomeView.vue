<template>
  <div class="home-view">
    <div class="menu-out">
      <div class="menu-in">
        <h1 class="h1-tag">오늘의 밥 친구를 찾아서 가보자굿 -0- ;;;;; ;; bb</h1>
        <div>
          <button @click="toChooseView" class="btn-com1 btn-blue">오늘의 밥친구는 ?! 얘는 로그인 했을 때만 가능</button>
          <button @click="toNormalMovieView" class="btn-com1">로그인 안해도 상관 X => 개무난한 추천페이지</button>
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
  height: 600px;
  background-color: #D6E7F6;
  border-radius: 20px 20px 0 0;
  position: relative;
}
.menu-in {
  width: 90%;
  height: 100%;
  position: absolute;
  left: 5%;
  top: 40px;
  border-radius: 20px 20px 0 0;
  background-color: #fff;
}

.btn-com1 {
  width: 72%;
  height: 100px;
  border-radius: 10px;
  border: none;
  margin-top: 20px;
  font-size: 24px;
}
.btn-blue {
  background-color: #2E8ADF;
  font-weight: bold;
  color: #fff;
}
</style>