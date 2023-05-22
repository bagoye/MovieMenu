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
    <div v-if="isEditMode">
      <input v-model="editedTitle" placeholder="수정할 제목" />
      <textarea v-model="editedContent" placeholder="수정할 내용"></textarea>
      <button @click="articleUpdate">저장</button>
      <button @click="cancelEdit">취소</button>
    </div>
    <div v-else>
      <button @click="toggleEditMode">수정</button>
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
      article: null,
      editedTitle: '', // 수정된 제목을 저장하는 변수
      editedContent: '', // 수정된 내용을 저장하는 변수
      isEditMode: false,
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
        this.editedTitle = res.data.title // 초기 제목 설정
        this.editedContent = res.data.content // 초기 내용 설정
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
        this.$store.commit('DELETE_ARTICLE', this.article) // Vuex에서 해당 게시글 제거
        this.article = null
        this.$router.push({name: 'FreeCommunityView'})
      })
      .catch((err) => {
        console.log(err)
      })
    },
    articleUpdate() {
      const updatedArticle = {
        title: this.editedTitle,
        content: this.editedContent,
      }
      axios({
        method: 'put',
        url: `${API_URL}/community/free/${this.$route.params.freepk}`,
        data: updatedArticle,
      })
      .then((res) => {
        console.log(res)
        this.article.title = this.editedTitle
        this.article.content = this.editedContent
        this.isEditMode = false
      })
      .catch((err) => {
        console.log(err)
      })
    },
    toggleEditMode() {
      this.isEditMode = true
    },
    cancelEdit() {
      this.isEditMode = false
    },
  },
}
</script>
