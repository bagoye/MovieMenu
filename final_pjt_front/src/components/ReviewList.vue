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
    }
  }
}
</script>

<style>

</style>
