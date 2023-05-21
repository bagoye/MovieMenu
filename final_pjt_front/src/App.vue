<template>
  <div id="app">
    <nav>
      <img src="./assets/dayoungsuyeom.png" class="logo-img" alt="logo" @click="toHome">

      <div class="nav-link">
        <router-link :to="{name: 'HomeView'}" exact-active-class="active-link">홈</router-link>
        <router-link :to="{name: 'RandomMovieView'}" exact-active-class="active-link">오늘의 추천</router-link>
        <router-link :to="{name: 'CommunityView'}" exact-active-class="active-link">커뮤니티</router-link>
        <span v-if="isLogin">
          <!-- 로그인 되어있을 때 -->
          <a href="#" @click.prevent="logout">로그아웃</a>
          <router-link :to="{
            name: 'ProfileView',
            params: {userid: user}}">
            <img src="#" alt="profile image">
          </router-link>
        </span>

        <span v-if="!isLogin">
          <!-- 로그인 되어있지 않을 때 -->
          <router-link :to="{name: 'LoginView'}" exact-active-class="active-link">로그인</router-link>
        </span>
       </div>

    </nav>

    <!-- divide-block == 위에 여백주기 위해서 (nav랑 content 겹침 방지) 수정해야됨 -->
    <div class="divide-block"></div>
    <router-view/>
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

#app {
  width: 1094px;
  margin: 0 auto;
}

h1 {
  font-size: 32px;
  font-weight: bold; /* 800 */
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
  z-index: 100;
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

.profile-btn {
  width: 36px;
  height: 36px;
  background-color: #ccc;
  border-radius: 50%;
}
</style>
