<template>
  <div>
    <form @submit.prevent="submitComment">
      <textarea @keyup.enter="submitComment" v-model="commentContent" placeholder="댓글을 작성해주세요"></textarea>
      <button type="submit">작성</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'FreeCommentForm',
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
        url: `${API_URL}/community/free/${this.$route.params.freepk}/comment/`,
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