<template>
  <div>
    ProfileView

    {{ user.pk }}
    {{ user }}
  </div>
</template>

<script>
export default {
    name: 'ProfileView',
    data() {
        return {
            user: this.$store.state.userInfo
        }
    }
}
</script>

<style>

</style>