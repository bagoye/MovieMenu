<template>
  <div class="together-comment-form">
    <form @submit.prevent="submitComment" class="row">
      <textarea class="col-10" @keyup.enter="submitComment" v-model="commentContent" placeholder="댓글을 작성해주세요"></textarea>
      <button type="submit" class="col-2 mx-auto">작성</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommentForm',
  data() {
    return {
      commentContent: ''
    }
  },
  methods: {
    submitComment() {
      const data = {
        content: this.commentContent
      }
      axios({
        method: 'post',
        url: `${API_URL}/community/together/${this.$route.params.togetherpk}/comment/`,
        data: data,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          console.log(res)
          // 댓글 작성 후에 댓글 목록을 갱신하기 위해 이벤트를 발생시킵니다.
          this.$emit('comment-posted')
          this.commentContent = '' // 댓글 내용 초기화
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
}
</script>

<style>
.together-comment-form {
  width: 100%;
  margin: 0 auto;
}
.together-comment-form textarea {
  border-radius: 10px;
}
</style>