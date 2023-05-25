<template>
  <div class="comment-list-item">
    <div v-if="!editing" class="row">
      <div class="comment-content col-8">
        {{ comment.content }}
      </div>
      <div class="buttons col-4">
        <button @click="startEditing">수정</button>
        <button @click="deleteComment(comment)">삭제</button>
      </div>
      <div class="clear"></div>
    </div>

    <div v-else>
      <form @submit.prevent="submitComment">
        <label for="content">Content:</label>
        <textarea @keyup.enter="submitComment" v-model="updatedCommentData.content" id="content"></textarea>
        <button type="submit">Submit</button>
        <button @click="cancelEditing">Cancel</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CommentListItem',
  props: {
    comment: Object,
  },
  data() {
    return {
      editing: false,
      updatedCommentData: {
        content: '',
      },
    };
  },
  methods: {
    startEditing() {
      this.editing = true;
      this.updatedCommentData.content = this.comment.content;
    },
    cancelEditing() {
      this.editing = false;
      this.updatedCommentData.content = '';
    },
    submitComment() {
      this.$emit('edit-comment', this.comment, this.updatedCommentData);
      this.cancelEditing();
    },
    deleteComment(comment) {
      this.$emit('delete-comment', comment);
    },
  },
};
</script>

<style>
.comment-list-item {
  width: 80%;
  height: 50px;
  
  margin: 0 auto;
}
</style>
