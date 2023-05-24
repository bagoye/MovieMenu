<template>
  <div class="choose-item col-sm-6 col-lg-4">
    {{ genre }}

  </div>
</template>

<script>
export default {
  name: 'ChooseItem',
  props: {
    genre: Number
  }
}
</script>

<style>

</style>