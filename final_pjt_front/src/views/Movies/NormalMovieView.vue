<template>
  <div>
    <div>
      영상
    </div>
    <NormalMovieList
      v-for="(keyword, index) in keywords" :key="`keyword-${index}`"
      :keyword="keyword"
    />
  </div>
</template>

<script>
import NormalMovieList from '@/components/NormalMovieList'

export default {
  name: 'NormalMovieView',
  components: {
    NormalMovieList
  },
  data() {
    return {
      keywords: ['popular', 'voteaverage', 'adventure', 'action' ,'sf']
    }
  },
}
</script>

<style>

</style>