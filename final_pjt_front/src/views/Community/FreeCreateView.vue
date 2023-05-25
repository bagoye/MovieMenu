<template>
  <div class="free-create-view">
    <h1>자유 게시글 <span class="text-blue">작성하기</span></h1>
    <div class="free-create-wrap">
      <form @submit.prevent="createArticle">
        <label for="title"><b>제목</b></label><br>
        <input type="text" id="title" class="mt-2" v-model.trim="title"><br>
        <label for="content" class="mt-4"><b>내용</b></label><br>
        <textarea id="content" class="mt-2" cols="30" rows="10" v-model="content"></textarea><br>
        <input type="submit" id="submit" class="my-4 submit-btn">
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CreateView',
  data() {
    return {
      title: null,
      content: null,
    }
  },
  methods: {
    createArticle() {
      const title = this.title
      const content = this.content

      if (!title) {
        alert('제목 입력해주세요')
        return
      } else if (!content){
        alert('내용 입력해주세요')
        return
      }

      axios({
        method: 'post',
        url: `${API_URL}/community/free/`,
        data: { title, content},
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        this.$router.push({name: 'FreeCommunityView'})
      })
      .catch((err) => {
        console.log(err)
        console.log('post에서 오류가 난닷')
      })
    }
  }
}
</script>

<style>
.free-create-wrap {
  margin-top: 50px;
  text-align: center;
}
.free-create-wrap * {
  width: 70%;
  margin: 0 auto;
  border-radius: 5px;
}

.free-create-wrap textarea, .free-create-wrap input {
  border: 1px solid #2E8ADF;
}

.free-create-wrap .submit-btn {
  background-color: #2E8ADF;
  color: #fff;
}
</style>