<template>
  <div class="login-view">
    <div class="menu-out">
      <div class="menu-in">
        <h1 class="mt-5">로그인</h1>

        <form @submit.prevent="login" class="mt-5">
          <div class="accounts-input">
            <label for="username">아이디</label>
            <input type="text" id="username" v-model="username"><br>
          </div>

          <div class="accounts-input">
            <label for="password">비밀번호</label>
            <input type="password" id="password" v-model="password"><br>
          </div>

          <input type="submit" value="로그인" class="login-btn btn-blue mt-4">
        </form>
        <button @click="signup" class="login-btn">회원가입</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    login() {
      const username = this.username
      const password = this.password

      const payload = {
        username, password
      }

      this.$store.dispatch('login', payload)

    },

    signup() {
      this.$router.push({name: 'SignupView'})
    }
  }
}
</script>

<style>
  .login-view {
    text-align: center;
  }

  .accounts-input {
    width: 50%;
    height: 48px;
    line-height: 48px;
    margin: 10px auto;
  }

  .accounts-input > label {
    width: 30%;
    text-align: left;
  }
  .accounts-input > input {
    width: 70%;
    height: 48px;
    padding: 10px;
    border-radius: 5px;
    border: 1px solid #2E8ADF;
  }

  .login-btn {
    width: 50%;
    height: 48px;
    border-radius: 5px;
    border: none;
    margin: 5px 0;
  }

  .login-btn:hover {
    font-weight: bold;
  }
  
</style>