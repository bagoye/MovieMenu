<template>
  <div>
    {{ review.content }}
    {{ review.score }}
  </div>
</template>

<script>
export default {
  name: 'ReviewListItem',
  props: {
    review: Object,
  }
}
</script>

<style>

</style>