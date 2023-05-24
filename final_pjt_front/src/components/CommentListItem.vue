<template>
  <div>
    <p>{{ comment.user }} - {{ comment.content }}</p>
    <hr />
  </div>
</template>

<script>
export default {
  name: 'CommentListItem',
  props: ['comment']
}
</script>

<style>

</style>
