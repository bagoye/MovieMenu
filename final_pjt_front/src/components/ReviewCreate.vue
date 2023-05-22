<template>
  <div>
    ReviewCreate
    <h1>리뷰 작성하기</h1>
    <form @submit.prevent="createReview">
      <label for="content">내용 : </label>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
      <label for="score">평점 : </label>
      <input type="number" id="score" min="0" max="5" step="0.5" v-model="score">
      <input type="submit" id="submit">
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
      const routeParamsPk = this.$route.params.pk

      if (!content) {
        alert('내용 입력해주세요')
        return
      }
      else if (!score){
        alert('평점 입력해주세요')
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
      .then(() => { 
        console.log('안녕하세요?')
      })
      .catch((err) => {
        console.log(err)
        console.log('안된다고ㅡㅡ')
        console.log(routeParamsPk)
      })
    }
  }
}
</script>

<style>

</style>