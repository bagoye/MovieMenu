<template>
  <div>
    ProfileUserSection

    <div>{{ user.pk }}</div>
    <div>{{ user.username }}</div>
    <div>{{ user.email }}</div>
    <div class="followers">
      팔로잉 :
      팔로워 :
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProfileUserSection',
  data() {
    return {
      user: this.$store.state.userInfo
    }
  }
}
</script>

<style>

</style>