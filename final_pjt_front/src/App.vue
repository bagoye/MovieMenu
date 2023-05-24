<template>
  <div id="app" class="row mx-auto">
    <nav class="navbar fixed-top navbar-expand-lg bg-body-tertiary mx-auto" style="max-width: 1200px;">
      <div class="container-fluid">
        <img src="./assets/dayoungsuyeom.png" class="logo-img navbar-brand" alt="logo" @click="toHome">
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarNav">
          <div class="nav-link">
            <router-link :to="{name: 'HomeView'}" exact-active-class="active-link">홈</router-link>
            <router-link :to="{name: 'RandomMovieView'}" exact-active-class="active-link">오늘의 추천</router-link>
            <router-link :to="{name: 'CommunityView'}" exact-active-class="active-link">커뮤니티</router-link>
            <span v-if="isLogin">
              <!-- 로그인 되어있을 때 -->
              <router-link :to="{
                name: 'ProfileView',
                params: {'userid': user}}"
                exact-active-class="active-link">
                마이페이지
              </router-link>
              <a href="#" @click.prevent="logout">로그아웃</a>
            </span>

            <span v-if="!isLogin">
              <!-- 로그인 되어있지 않을 때 -->
              <router-link :to="{name: 'LoginView'}" exact-active-class="active-link">로그인</router-link>
            </span>
          </div>
        </div>
      </div>
    </nav>

    <!-- divide-block == 위에 여백 (nav랑 content 겹침 방지) -->
    <div class="divide-block"></div>

    <div class="content-wrapper">
      <router-view class="col-12" :class="{ 'full-width': $route.meta.fullWidth }"/>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'app',
  data() {
    return {
      user: this.$store.state.userInfo.pk
    }
  },
  created() {
    this.$store.dispatch('getUserInfo')
    console.log(this.user.data)

  },
  computed: {
    ...mapGetters(['isLogin']),
  },
  methods: {
    toHome() {
      this.$router.push({name: 'HomeView'}).catch(() => {})
    },
    toProfile() {
      this.$router.push({name: 'ProfileView'}).catch(() => {})
    },
    ...mapActions(['logout',]),
    
  }
}
</script>

<style>
* {
  font-family: "Elice Digital Baeum", sans-serif;
}

body {
  background-color: #FFFBEF;
}

h1 {
  font-size: 28px;
  font-weight: bold;
}

.logo-img {
  cursor: pointer;
}

nav {
  height: 150px;
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
  font-weight: bold;
  font-size: 16px;
  color: #000;
  text-decoration: none;
}
.nav-link *:hover {
  color: #2E8ADF;
}
.active-link {
  color: #2E8ADF;
}

.nav-link > span {
  margin-left: 0;
}


/* 스크롤바 없애기 */
body{
 -ms-overflow-style: none;
 }
 
::-webkit-scrollbar {
  display: none;
}

/* 필요할 때, bind로 full width on-off */
.content-wrapper {
  max-width: 1094px;
  margin: 0 auto;
}
.full-width {
  max-width: none;
  left: 0;
}
</style>
