<template>
  <div class="review-create">
    <div><b>리뷰 작성하기</b></div>
    <form @submit.prevent="createReview" class="review-form row">
      <label for="score" class="col-1"><b>평점</b></label>
      <input type="number" id="score" min="0" max="5" step="0.5" v-model="score" class="col-3">
      <label for="content" class="col-1"><b>내용</b></label>
      <textarea @keyup.enter="createReview" class="col-6" id="content" cols="30" rows="10" v-model="content"></textarea><br>
      <input type="submit" id="submit" value="저장" class="col-1 save-btn">
    </form>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'ReviewCreate',
    data() {
        return {
            content: null,
            score: null,
        }
    },
    created() {
      console.log(this.$store.state.token)
    },
    methods: {
    createReview() {
      const content = this.content
      const score = parseFloat(this.score)
      // const routeParamsPk = this.$route.params.pk
      const routeParamsPk = this.$route.params.pk

      if (!content) {
        alert('내용을 입력해주세요')
        return
      }
      else if (!score){
        alert('평점을 입력해주세요')
        return
      }

      axios({
        method: 'post',
        url: `${API_URL}/movies/review/${routeParamsPk}/`,
        // url: `${API_URL}/movies/review/`,
        data: {content, score},
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((response) => {
        const review = response.data;
        this.$store.dispatch('addReviewToMovie', { movieId: routeParamsPk, review });
        this.content = null;
        this.score = null;
        this.$store.dispatch('getReviews', routeParamsPk);
        // this.$router.replace({ name: 'MovieDetailView', params: { pk: routeParamsPk } }).catch(() => {});
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>

<style>
.review-form {
  width: 100%;
  height: 100px;
  margin-top: 20px;
  background-color: #fff;
  border-radius: 10px;
  text-align: center;
}

.review-form label {
  line-height: 100px;
}

.review-form input, .review-form textarea{
  height: 70px;
  margin-top: 15px;
  border-radius: 5px;
}
.save-btn {
  width: 60px;
  margin: 0 auto;
}
</style>