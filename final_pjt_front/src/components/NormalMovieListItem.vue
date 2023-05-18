<template>
  <div>
    {{ movie.title }}

  </div>
</template>

<script>
export default {
  name: 'NormalMovieListItem',
  props: {
    movie: Object,
  }
}
</script>

<style>

</style>