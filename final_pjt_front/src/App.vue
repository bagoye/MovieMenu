<template>
  <div id="app">
    <nav>
      <img src="#" alt="logo">

      <div>
        <router-link to='/'>HOME</router-link> |
        <router-link :to="{name: 'RandomMovieView'}">오늘의 추천</router-link> |
        <router-link :to="{name: 'CommunityView'}">커뮤니티</router-link> |
        <router-link :to="{name: 'AccountView'}">Login</router-link>
        <!-- 회원가입은 로그인 페이지 들어가있을 때 보일거임 -->
        <!-- <router-link to="/">Logout</router-link> | -->
        <!-- 로그아웃, 로그인은 로그인 돼있을 때 떠야해서 v-if로 조건 줘야할듯 -->
        <a href="#"><img src="#" alt="profile image">프로필</a>
      </div>

    </nav>
    <router-view/>
  </div>
</template>

<style>

</style>
