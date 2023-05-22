<template>
  <div>
    ReviewList
    <ReviewListItem 
      v-for="(review, index) in reviews" :key="`review-${index}`"
      :review="review"
    />
    <ReviewCreate />
  </div>
</template>

<script>
import ReviewListItem from '@/components/ReviewListItem'
import ReviewCreate from '@/components/ReviewCreate'

export default {
  name: 'ReviewList',
  components: {
      ReviewListItem,
      ReviewCreate,
  },
  computed: {
    reviews() {
      return this.$store.state.reviews
    },
  },
  created() {
    console.log(this.$route.params.pk, '####')
    this.$store.dispatch('getReviews', this.$route.params.pk)
  }
}
</script>

<style>

</style>
