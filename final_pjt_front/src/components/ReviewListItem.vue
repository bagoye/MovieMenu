<template>
  <div class="review-item">
    <div v-if="!editing" class="row text-center">
      <div class="col-1"><b>{{ review.user.username }}</b></div>
      <div class="col-7">{{ review.content }}</div>
      <div class="col-2">평점 : {{ review.score }}</div>
      <div class="review-item-btn col-2">
        <button @click="startEditing" class="edit-btn">수정</button>
        <button @click="deleteReview(review)" class="del-btn">삭제</button>
      </div>
      <hr>
    </div>

    <div v-else class="edit-form text-center">
      <div class="review-text">리뷰 수정하기</div>
      <form @submit.prevent="submitReview" class="row">
        <label for="content" class="col-1">내용</label>
        <textarea @keyup.enter="submitReview" v-model="updatedReviewData.content" id="content" class="col-6"></textarea>
        <label for="score" class="col-1">평점</label>
        <input v-model="updatedReviewData.score" type="number" id="score" min="0" max="5" step="0.5" class="col-2">
        <div class="edit-form-btn col-2">
          <button type="submit" class="edit-btn">수정</button>
          <button @click="cancelEditing">취소</button>
        </div>
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
.review-item {
  font-size: 16px;
  width: 100%;
  height: 70px;
  line-height: 70px;
  position: relative;
}
.review-item-btn button {
  width: 60px;
  height: 36px;
  line-height: 0;
  margin: 0 5px;
  border: none;
  border-radius: 5px;
}

.edit-form {
  padding: 10px;
  background-color: #FFFBEF;
  position: absolute;
  top: 0;
  left: 0;
  z-index: 99;

  border-radius: 10px;
}

.edit-form form * {
  height: 44px;
  line-height: 44px;
}
.edit-form form textarea input button {
  line-height: 0;
}

.review-text {
  font-weight: bold;
}

.review-item .edit-form button {
  margin: 0 5px;
  line-height: 0;
  border-radius: 5px;
}
.review-item .edit-form {
  width: 100%;
}
.review-item .edit-form textarea, .review-item .edit-form input {
  border-radius: 5px;
}

</style>