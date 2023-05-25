<template>
  <div class="profile-view">
    <div class="menu-out">
      <div class="menu-in">
        <ProfileUserSection class="mt-5" />
      </div>
    </div>
  </div>
</template>

<script>
import ProfileUserSection from '@/components/ProfileUserSection'

export default {
  name: 'ProfileView',
  components: {
    ProfileUserSection,
  },
  computed: {
    reviews() {
      return this.$store.state.reviews
    }
  }

}
</script>

<style>

</style>