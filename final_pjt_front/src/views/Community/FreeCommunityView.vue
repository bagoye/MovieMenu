<template>
  <div class="free-community-view">
    <span v-if="isLogin">
      <router-link :to="{name : 'FreeCreateView'}"><button>작성하기</button></router-link>
    </span>

    <ArticleList class="mt-4 clear"/>
  </div>
</template>

<script>
import ArticleList from '@/components/ArticleList'
import { mapGetters } from 'vuex'

export default {
  name: 'FreeCommunityView',
  components: {
    ArticleList,
  },
  computed: {
    ...mapGetters(['isLogin']),
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles() {
      this.$store.dispatch('getArticles')
    }
  }
}
</script>

<style>
.free-community-view {
  width: 100%;
}

.free-community-view button {
  width: 100px;
  height: 44px;
  border-radius: 10px;
  border: none;

  float: right;
  margin-bottom: 30px;
  margin-right: 30px;
}
.free-community-view button:hover {
  color: #fff;
  background-color: #2E8ADF;
}
</style>