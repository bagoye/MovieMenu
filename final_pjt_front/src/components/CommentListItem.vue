<template>
  <div class="comment-list-item">
    <div v-if="!editing" class="row">
      <div class="comment-content col-8">
        {{ comment.content }}
      </div>
      <div class="buttons col-4">
        <button @click="startEditing" class="edit-btn">수정</button>
        <button @click="deleteComment(comment)" class="del-btn">삭제</button>
      </div>
      <div class="clear"></div>
    </div>

    <div v-else class="edit-form text-center">
      <div class="review-text mt-5">댓글 수정하기</div>
      <form @submit.prevent="submitComment" class="row mt-5">
        <label for="content" class="col-1">내용</label>
        <textarea @keyup.enter="submitComment" v-model="updatedCommentData.content" id="content" class="col-8"></textarea>
        <button type="submit" class="col-1 edit-btn">수정</button>
        <button @click="cancelEditing" class="col-1">취소</button>
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
  width: 100%;
  height: 50px;
  
  margin: 0 auto;
  position: relative;
}
.comment-content {
  line-height: 50px;
}
.comment-list-item .edit-form button {
  line-height: 0;
}
.comment-list-item .edit-form textarea {
  border-radius: 5px;
}

</style>
