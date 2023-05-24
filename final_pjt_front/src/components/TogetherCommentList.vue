<template>
  <div>
    <div>
      <p>TogetherCommentList</p>
      <div v-for="comment in comments" :key="comment.id">
        <CommentListItem :comment="comment" @edit-comment="editComment" @delete-comment="deleteComment" />
      </div>
    </div>
    <TogetherCommentForm @comment-posted="refreshComments" />
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

import CommentListItem from '@/components/CommentListItem'
import TogetherCommentForm from '@/components/TogetherCommentForm'

export default {
  name: 'TogetherCommentList',
  components: {
    CommentListItem,
    TogetherCommentForm
  },
  data() {
    return {
      comments: []
    }
  },
  created() {
    this.getTogetherComments()
  },
  methods: {
    getTogetherComments() {
      axios({
        method: 'get',
        url: `${API_URL}/community/together/${this.$route.params.togetherpk}/comment/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          console.log(res)
          this.comments = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    refreshComments() {
      this.getTogetherComments()
    },
    editComment(comment, updatedCommentData) {
      if (comment.user !== this.$store.state.userInfo?.pk) {
        // 작성자가 아닌 경우 알림을 띄웁니다.
        alert("작성자만 수정할 수 있습니다.");
        return;
      }

      axios({
        method: 'put',
        url: `${API_URL}/community/together/${this.$route.params.togetherpk}/${comment.id}/`,
        data: {
          content: updatedCommentData.content
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          console.log(res)
          const updatedComment = res.data
          const index = this.comments.findIndex(c => c.id === updatedComment.id)
          if (index !== -1) {
            this.$set(this.comments, index, updatedComment)
          }
        })
        .catch((err) => {
          console.log(err)
        })
    },
    deleteComment(comment) {
      if (comment.user !== this.$store.state.userInfo?.pk) {
        // 작성자가 아닌 경우 알림을 띄웁니다.
        alert("작성자만 삭제할 수 있습니다.");
        return;
      }

      axios({
        method: 'delete',
        url: `${API_URL}/community/together/${this.$route.params.togetherpk}/${comment.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          console.log(res)
          const index = this.comments.findIndex(c => c.id === comment.id)
          if (index !== -1) {
            this.comments.splice(index, 1)
          }
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
}
</script>

<style>
/* Add necessary styling here */
</style>
