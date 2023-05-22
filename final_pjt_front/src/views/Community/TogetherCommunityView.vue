<template>
  <div>
    TogetherCommunityView
    <span v-if="isLogin">
      <router-link :to="{name : 'TogetherCreateView'}">[CREATE]</router-link>
    </span>
    <TogetherList/>
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

</style>