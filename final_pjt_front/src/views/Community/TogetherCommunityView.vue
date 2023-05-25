<template>
  <div class="together-community-view">
    <span v-if="isLogin">
      <router-link :to="{name : 'TogetherCreateView'}"><button>작성하기</button></router-link>
    </span>

    <TogetherList class="mt-4 clear"/>
  </div>
</template>

<script>
import TogetherList from '@/components/TogetherList'
import { mapGetters } from 'vuex'

export default {
  name: 'TogetherCommunityView',
  components: {
    TogetherList,
  },

  computed: {
    ...mapGetters(['isLogin']),
  },
  created() {
    this.getArticlesTogether()
  },
  methods: {
    getArticlesTogether() {
      this.$store.dispatch('getArticlesTogether')
    }
  }
}
</script>

<style>
.together-community-view {
  width: 100%;
}

.together-community-view button {
  width: 100px;
  height: 44px;
  border-radius: 10px;
  border: none;

  float: right;
  margin-bottom: 30px;
  margin-right: 30px;
}
.together-community-view button:hover {
  color: #fff;
  background-color: #2E8ADF;
}
</style>