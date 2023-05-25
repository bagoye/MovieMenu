<template>
  <div class="free-detail-view">
    <div class="menu-out">
      <div class="menu-in">
        <div class="article-wrap">    
          <div>
            <div class="article-title mt-5">
              <div class="board">자유 게시판</div>
              <div class="article">{{ article?.title }}</div>
              <p class="created">작성시간 : {{ article?.created_at|formatDate }}</p>
              <p class="clear"></p>
            </div>
            <div class="article-content">
              <p class="content-label">내용</p>
              <p>{{ article?.content }}</p>
            </div>
          </div>

          <div v-if="isEditMode" class="edit-form row">
            <p class="mt-4"><b>게시글 수정하기</b></p>
            <label for="edit-title" class="col-1">제목</label>
            <input id="edit-title" v-model="editedTitle" placeholder="수정할 제목" class="col-3" />
            <label for="edit-content" class="col-1">내용</label>
            <textarea id="edit-content" v-model="editedContent" placeholder="수정할 내용" class="col-7"></textarea>
            <div class="mt-4">
              <button @click="articleUpdate" class="edit-btn">수정</button>
              <button @click="cancelEdit">취소</button>
            </div>
            <div class="clear"></div>
          </div>

          <div v-else class="buttons">
            <button @click="toggleEditMode" class="edit-btn">수정</button>
            <button @click="articleDelete" class="del-btn">삭제</button>
          </div>
          <div class="clear"></div>
          <FreeCommentList class="my-5"/>

          <router-link
            :to="{name:'FreeCommunityView'}">
              <button style="width:100px;" class="mb-5">뒤로가기</button> 
          </router-link>
        </div>
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import FreeCommentList from '@/components/FreeCommentList'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'FreeDetailView',
  components: {
    FreeCommentList
  },
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
        const userId = res.data.userid
        const currentUserId = this.$store.state.userInfo?.pk
        if (userId !== currentUserId) {
          this.isEditMode = false
        }
        console.log(this.article.user)
        console.log(this.$store.state.userInfo?.pk)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    articleDelete() {
      // 글 작성자와 로그인한 사용자를 비교하여 권한을 확인
      if (this.article.user !== this.$store.state.userInfo?.pk) {
        // 작성자가 아닌 경우 알림을 띄웁니다.
        alert("작성자만 삭제할 수 있습니다.");
        return;
      }
      axios({
        method: 'delete',
        url: `${API_URL}/community/free/${ this.$route.params.freepk }`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
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
        url: `${API_URL}/community/free/${this.$route.params.freepk}`,
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
  },
}
</script>

<style>
.free-detail-view {
  text-align: center;
}

.article-wrap {
  width: 90%;
  margin: 0 auto;
}


.article-title {
  text-align: left;
  margin-left: 30px;
}
.article-title .board {
  font-size: 24px;
}
.article-title .article {
  font-size: 32px;
  font-weight: bold;
  color: #2E8ADF;
}

.article-content {
  width: 80%;
  margin: 0 auto;
  text-align: left;
  font-size: 16px;
}
.content-label {
  font-weight: bold;
}

.created {
  float: right;
  font-size: 14px;
  color: #666;
}

/* 컨텐츠 내에 있는 버튼들 */
.article-wrap button {
  border: none;
  width: 70px;
  height: 36px;
  border-radius: 5px;
  margin: 5px;
}

.buttons {
  float: right;
}

.article-wrap {
  position: relative;
}

.free-detail-view .edit-form {
  top: 0;
  left: 10px;
  width: 100%;
  height: 280px;
  position: absolute;
}

</style>