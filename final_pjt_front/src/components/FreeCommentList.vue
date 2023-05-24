<template>
  <div>
    <div>
      <p>FreeCommentList</p>
      <div v-for="comment in comments" :key="comment.id">
        <CommentListItem :comment="comment" />
      </div>
    </div>
    <FreeCommentForm @comment-posted="refreshComments" />
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

import CommentListItem from '@/components/CommentListItem' // CommentListItem 컴포넌트 import
import FreeCommentForm from '@/components/FreeCommentForm' // CommentForm 컴포넌트 import

export default {
  name: 'FreeCommentList',
  components: {
    CommentListItem, // CommentListItem 컴포넌트 등록
    FreeCommentForm // CommentForm 컴포넌트 등록
  },
  data() {
    return {
      comments: []
    }
  },
  created() {
    this.getFreeComments()
  },
  methods: {
    getFreeComments() {
      axios({
        method: 'get',
        url: `${API_URL}/community/free/${this.$route.params.freepk}/comment/`,
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
      this.getFreeComments()
    }
  }
}
</script>

<style>

</style>
