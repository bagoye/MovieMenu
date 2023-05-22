<template>
  <div>
    <div>
      <h1>FreeDetailView</h1>
      <p>글 번호 : {{ article?.id }}</p>
      <p>제목 : {{ article?.title }}</p>
      <p>내용 : {{ article?.content }}</p>
      <p>작성시간 : {{ article?.created_at }}</p>
      <p>수정시간 : {{ article?.updated_at }}</p>
    </div>
    <div>
      <button @click="articleDelete">삭제</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'FreeDetailView',
  data() {
    return {
      article: null
    }
  },
  created() {
    this.getArticleDetail()
  },
  methods: {
    getArticleDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/community/free/${ this.$route.params.freepk }`,
      })
      .then((res) => {
        console.log(res)
        this.article = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    articleDelete() {
      axios({
        method: 'delete',
        url: `${API_URL}/community/free/${ this.$route.params.freepk }`,
      })
      .then((res) => {
        console.log(res)
        this.$store.dispatch('getArticles') // 게시글 목록 갱신
        this.article = null
        localStorage.removeItem('article') // 로컬 스토리지에서 삭제
        this.$router.push({ name: 'FreeCommunityView' })
        // localStorage.removeItem('article')
        // this.article = null
        // this.$router.push({name: 'FreeCommunityView'})
        // this.$store.dispatch('getArticles')
      })
      .catch((err) => {
        console.log(err)
      })
    }
    
  }
}
</script>
