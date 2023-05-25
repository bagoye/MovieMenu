<template>
  <div class="review-list">
    <div><b>리뷰</b></div>
    <div class="review-wrap">
      <ReviewListItem 
        v-for="(review, index) in reviews" :key="`review-${index}`"
        :review="review"
      />
      <ReviewCreate  class="mt-3"/>
    </div>
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
    const movieId = this.$route.params.pk;
    this.$store.dispatch('getReviews', movieId);
  }
}
</script>

<style>
.review-wrap {
  margin-top: 10px;
  width: 100%;
  background-color: #D6E7F6;
  padding: 20px 40px;
  border-radius: 10px;
}
</style>
