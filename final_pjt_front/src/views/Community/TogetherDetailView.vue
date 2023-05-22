<template>
  <div>
    <div>
      <h1>TogetherDetailView</h1>
      <p>글 번호 : {{ article?.id }}</p>
      <p>제목 : {{ article?.title }}</p>
      <p>내용 : {{ article?.content }}</p>
      <p>작성시간 : {{ article?.created_at }}</p>
      <p>수정시간 : {{ article?.updated_at }}</p>
      <!-- <p>영화제목: {{ resultMovie ? resultMovie.title : '' }}</p>
      <p>영화 포스터: {{ resultMovie ? resultMovie.poster_path : '' }}</p> -->
      <p v-if="resultMovie">영화제목: {{ resultMovie.title }}</p>
      <p v-if="resultMovie">영화 포스터: {{ resultMovie.poster_path }}</p>
    </div>
    <div v-if="isEditMode">
      <input v-model="editedTitle" placeholder="수정할 제목" />
      <textarea v-model="editedContent" placeholder="수정할 내용"></textarea>
      <button @click="togetherArticleUpdate">저장</button>
      <button @click="cancelEdit">취소</button>
    </div>
    <div v-else>
      <button @click="toggleEditMode">수정</button>
      <button @click="togetherArticleDelete">삭제</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapGetters } from 'vuex'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'TogetherDetailView',
  data() {
    return {
      article: null,
      editedTitle: '', // 수정된 제목을 저장하는 변수
      editedContent: '', // 수정된 내용을 저장하는 변수
      isEditMode: false,
    }
  },
  created() {
    this.getTogetherArticleDetail()
    // this.resultMovie = this.article.searchResult
  },
  computed: {
    ...mapGetters(['getResultMovie']),
    resultMovie() {
      return this.$store.getters.getResultMovie;
    }
  },
  methods: {
    getTogetherArticleDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/community/together/${ this.$route.params.togetherpk }`,
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
    togetherArticleDelete() {
      // 글 작성자와 로그인한 사용자를 비교하여 권한을 확인
      if (this.articlesTogether.user !== this.$store.state.userInfo?.pk) {
        // 작성자가 아닌 경우 알림을 띄웁니다.
        alert("작성자만 삭제할 수 있습니다.");
        return;
      }
      axios({
        method: 'delete',
        url: `${API_URL}/community/together/${ this.$route.params.togetherpk }`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        console.log(res)
        this.$store.commit('DELETE_ARTICLE_TOGETHER', this.article) // Vuex에서 해당 게시글 제거
        this.article = null
        this.$router.push({name: 'TogetherCommunityView'})
      })
      .catch((err) => {
        console.log(err)
      })
    },
    togetherArticleUpdate() {
      // 글 작성자와 로그인한 사용자를 비교하여 권한을 확인
      if (this.articlesTogether.user !== this.$store.state.userInfo?.pk) {
        // 작성자가 아닌 경우 알림을 띄웁니다.
        alert("작성자만 수정할 수 있습니다.");
        return;
      }

      const updatedArticle = {
        title: this.editedTitle,
        content: this.editedContent,
      }
      axios({
        method: 'put',
        url: `${API_URL}/community/together/${this.$route.params.togetherpk}`,
        data: updatedArticle,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
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
