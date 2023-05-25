<template>
  <div>
    ProfileView
    <ProfileUserSection />

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