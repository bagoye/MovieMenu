<template>
  <div>
    <div v-if="!editing">
      {{ comment.content }}
      <button @click="startEditing">Edit</button>
      <button @click="deleteComment(comment)">Delete</button>
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
/* Add necessary styling here */
</style>
