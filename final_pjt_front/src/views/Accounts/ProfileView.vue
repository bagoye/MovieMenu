<template>
  <div>
    ProfileView
    <ProfileUserSection />
    <div class="profile-review">
      <ReviewListItem
        v-for="(review, index) in reviews" :key="`review-${index}`"
        :review="review"
      />
    </div>
  </div>
</template>

<script>
import ProfileUserSection from '@/components/ProfileUserSection'
import ReviewListItem from '@/components/ReviewListItem'

export default {
  name: 'ProfileView',
  components: {
    ProfileUserSection,
    ReviewListItem
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