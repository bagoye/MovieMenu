<template>
  <div>
    <router-link 
    :to="{
      name:'MovieDetailView', 
      params: { pk: movie.id }}">
      <img :src="`https://image.tmdb.org/t/p/w300_and_h450_bestv2${movie.poster_path}`">
    </router-link>

    {{ movie.title }}
  </div>
</template>

<script>
export default {
  name: 'ChooseMovieItem',
  props: {
    movie: Object
  },


}
</script>

<style>

</style>