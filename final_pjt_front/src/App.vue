<template>
  <div id="app">
    <nav>
      <img src="./assets/dayoungsuyeom.png" class="logo-img" alt="logo" @click="toHome">

      <div class="nav-link">
        <router-link :to="{name: 'HomeView'}">홈</router-link>
        <router-link :to="{name: 'RandomMovieView'}">오늘의 추천</router-link>
        <router-link :to="{name: 'CommunityView'}">커뮤니티</router-link>
        <router-link :to="{name: 'AccountView'}">로그인</router-link>
        <!-- 회원가입은 로그인 페이지 들어가있을 때 보일거임 -->
        <!-- <router-link to="/">Logout</router-link> | -->
        <!-- 로그아웃, 로그인은 로그인 돼있을 때 떠야해서 v-if로 조건 줘야할듯 -->
        <a href="#" class="profile-btn"><img src="#" alt="profile image" v-if="img">dd</a>
      </div>

    </nav>
    <div class="divide-block"></div>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'app',
  methods: {
    toHome() {
      this.$router.push({name: 'HomeView'}).catch(() => {})
    }
  }
}
</script>

<style>
body {
  background-color: #FFFBEF;
}

#app {
  width: 1094px;
  margin: 0 auto;
}

.logo-img {
  height: 45%;
  cursor: pointer;
}

nav {
  width: 1094px;
  height: 150px;
  display: flex;
  align-items: center;

  position: fixed;
  top: 0;
}

.divide-block {
  width: 100%;
  height: 150px;
}

.nav-link {
  width: 100%;
  text-align: right;
}

.nav-link * {
  margin-left: 40px;
  font-size: 16px;
  color: #000;
  text-decoration: none;
}

.profile-btn {
  width: 36px;
  height: 36px;
  background-color: #ccc;
  border-radius: 50%;
}
</style>
