<template>
  <div>
    TogetherCommentList
    <CommentListItem/>
    <CommentForm/>
  </div>
</template>

<script>
import CommentListItem from '@/components/CommentListItem.vue'
import CommentForm from '@/components/CommentForm.vue'
export default {
  name: 'TogetherCommentList',
  components: { 
    CommentListItem,
    CommentForm,
   },
}
</script>

<style>

</style>