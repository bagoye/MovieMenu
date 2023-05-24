<template>
  <div>
    <div v-if="!editing">
      리뷰: {{ review.content }}
      평점: {{ review.score }}
      작성자: {{ review.user.username }}
      <button @click="startEditing">Edit</button>
      <button @click="deleteReview(review)">Delete</button>
    </div>
    <div v-else>
      <form @submit.prevent="submitReview">
        <label for="content">Content:</label>
        <textarea @keyup.enter="submitReview" v-model="updatedReviewData.content" id="content"></textarea>
        <label for="score">Score:</label>
        <input v-model="updatedReviewData.score" type="number" id="score" min="0" max="5" step="0.5">
        <button type="submit">Submit</button>
        <button @click="cancelEditing">Cancel</button>
      </form>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'ReviewListItem',
  props: {
    review: Object,
  },
  computed: {
    ...mapGetters(['reviews']),
  },
  data() {
    return {
      editing: false,
      updatedReviewData: {
        content: '',
        score: null,
      },
    };
  },
  methods: {
    startEditing() {
      this.editing = true;
      this.updatedReviewData.content = this.review.content;
      this.updatedReviewData.score = this.review.score;
    },
    cancelEditing() {
      this.editing = false;
      this.updatedReviewData.content = '';
      this.updatedReviewData.score = null;
    },
    submitReview() {
    if (this.isAuthor(this.review)) {
      // 리뷰 수정 작업 수행
      // 수정된 리뷰 데이터와 리뷰의 고유 식별자를 액션에 전달
      this.$store.dispatch('updateReview', {
        movieId: this.$route.params.pk,
        reviewId: this.review.id,
        reviewData: this.updatedReviewData,
      }).then(() => {
        // 액션이 완료된 후에 데이터를 직접 업데이트합니다.
        const updatedReviewIndex = this.reviews.findIndex(r => r.id === this.review.id);
        if (updatedReviewIndex !== -1) {
          this.$set(this.reviews, updatedReviewIndex, {
            ...this.reviews[updatedReviewIndex],
            ...this.updatedReviewData,
          });
        }
        this.cancelEditing();
      }).catch(error => {
        // 리뷰 수정 중에 에러가 발생한 경우
        console.error(error);
        alert('리뷰 수정 중에 오류가 발생했습니다.');
      });
    } else {
      alert('작성자만 리뷰를 수정할 수 있습니다.');
    }
  },

    deleteReview(review) {
      if (this.isAuthor(this.review)) {
        // 리뷰 삭제 작업 수행
        // 리뷰의 고유 식별자를 액션에 전달
        this.$store.dispatch('deleteReview', {
          movieId: this.$route.params.pk,
          reviewId: review.id,
        }).then(() => {
          // 액션이 완료된 후에 데이터를 직접 업데이트합니다.
          const deletedReviewIndex = this.reviews.findIndex(r => r.id === review.id);
          if (deletedReviewIndex !== -1) {
            this.reviews.splice(deletedReviewIndex, 1);
          }
        }).catch(error => {
          // 리뷰 삭제 중에 에러가 발생한 경우
          console.error(error);
          alert('리뷰 삭제 중에 오류가 발생했습니다.');
        });
      } else {
        alert('작성자만 리뷰를 삭제할 수 있습니다.');
      }
    },
    isAuthor(review) {
    // 현재 사용자와 리뷰의 작성자를 비교하여 작성자 여부를 확인합니다.
    // 작성자이면 true를 반환하고, 그렇지 않으면 false를 반환합니다.
      return review.user.id === this.$store.state.userInfo.pk;
    },    
  },
};
</script>

<style>
/* 필요한 스타일링 작업 수행 */
</style>