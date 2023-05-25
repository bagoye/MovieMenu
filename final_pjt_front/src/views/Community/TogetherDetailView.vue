<template>
  <div class="together-detail-view">
    <div class="menu-out">
      <div class="menu-in">
        <div class="article-wrap">    
          <div>
            <div class="article-title mt-5">
              <div class="board">영화 같이 봐요</div>
              <div class="article">{{ article?.title }}</div>
              <p class="created">작성시간 : {{ article?.created_at|formatDate }}</p>
              <p class="clear"></p>
            </div>
            
            <div class="article-content">
              <p>내용 : {{ article?.content }}</p>
              <p>수정시간 : {{ article?.updated_at }}</p>
              <div>
                <p>영화제목 : {{ getMovie[0].title }} </p>
                <img :src="`https://image.tmdb.org/t/p/w300_and_h450_bestv2${getMovie[0].poster_path}`">
                <p>줄거리 : {{ getMovie[0].overview|truncateText(100) }}</p>
                <p>평점 : {{ getMovie[0].vote_average }}</p>
                <p>런타임 : {{ getMovie[0].runtime }}분</p>
              </div>
            </div>
            <!-- article?.movie는 movie의 id -->
            <!-- <p> {{ allMovies }}</p> -->
          </div>
          <div v-if="isEditMode" class="edit-form row">
            <p><b>수정하기</b></p>
            <input v-model="editedTitle" placeholder="수정할 제목" />
            <textarea v-model="editedContent" placeholder="수정할 내용"></textarea>
            <button @click="togetherArticleUpdate">수정</button>
            <button @click="cancelEdit">취소</button>
          </div>
          <div v-else class="buttons">
            <button @click="toggleEditMode">수정</button>
            <button @click="togetherArticleDelete">삭제</button>
          </div>
          <div>
            <TogetherCommentList class="clear my-3"/>
          </div>
          <router-link
            :to="{name:'TogetherCommunityView'}">
              <button style="width:100px;">뒤로가기</button> 
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapGetters } from 'vuex'
import TogetherCommentList from '@/components/TogetherCommentList'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'TogetherDetailView',
  components: {
    TogetherCommentList
  },
  data() {
    return {
      allMovies: null,
      article: null,
      editedTitle: '', // 수정된 제목을 저장하는 변수
      editedContent: '', // 수정된 내용을 저장하는 변수
      isEditMode: false,

      getMovie: null,
    }
  },
  created() {
    this.getTogetherArticleDetail()
    
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/movies/allmovie/`,
    })
    .then(res => {
      console.log(res)
      this.allMovies = res.data
      this.searchResultMovie()
    })
    .catch(err => {
      console.log(err)
    })

    // this.searchResultMovie()
    
  },
  computed: {
    ...mapGetters(['selectMovie']),
    resultMovie() {
      return this.$store.getters.selectMovie;
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
        this.selectMovie(res.data); // 영화 정보 설정
      })
      .catch((err) => {
        console.log(err)
      })
    },
    togetherArticleDelete() {
      // 글 작성자와 로그인한 사용자를 비교하여 권한을 확인
      if (this.article.user !== this.$store.state.userInfo?.pk) {
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
      if (this.article.user !== this.$store.state.userInfo?.pk) {
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

    //
    searchResultMovie() {
    if (this.allMovies && this.article) {
      this.getMovie = this.allMovies.filter((movie) =>
        movie.id === this.article.movie
        );
      }
    },
  },
  filters: {
    formatDate(value) {
      const date = new Date(value);
      const year = date.getFullYear();
      const month = String(date.getMonth() + 1).padStart(2, '0');
      const day = String(date.getDate()).padStart(2, '0');
      const hours = String(date.getHours()).padStart(2, '0');
      const minutes = String(date.getMinutes()).padStart(2, '0');
      return `${year}-${month}-${day} ${hours}:${minutes}`;
    },
    truncateText(value, maxLength) {
      if (value.length <= maxLength) {
        return value;
      }
      return value.substring(0, maxLength) + '...';
    },
  },
}
</script>
