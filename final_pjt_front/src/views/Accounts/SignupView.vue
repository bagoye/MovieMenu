<template>
  <div class="signup-view">
    <div class="menu-out">
      <div class="menu-in">
        <h1 class="mt-5">회원가입</h1>
        <form @submit.prevent="signUp" class="mt-5">
          <div class="accounts-input">
            <label for="username">아이디</label>
            <input type="text" id="username" v-model="username"><br>
          </div>
          <div class="accounts-input">
            <label for="password1">비밀번호</label>
            <input type="password" id="password1" v-model="password1"><br>
          </div>
          <div class="accounts-input">
            <label for="password2">비밀번호 확인</label>
            <input type="password" id="password2" v-model="password2">
          </div>

          <input type="submit" value="회원가입" class="login-btn btn-blue mt-4">
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    signUp() {
      
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2
      
      const payload = {
        username, password1, password2,
      }

      this.$store.dispatch('signUp', payload)

    }
  }
}
</script>

<style>
.signup-view {
    text-align: center;
  }
</style>