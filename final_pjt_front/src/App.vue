<template>
  <div id="app">
    <nav>
      <img src="" alt="logo">
      <div>
        <router-link :to="{name: 'HomeView'}">home</router-link>
        <router-link :to="{name: 'CommunityView'}">community</router-link>
        <router-link :to="{name: 'AccountView'}">Login</router-link>
        <!-- <router-link>signup</router-link> -->
        <router-link>profile</router-link>
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<style>

</style>
