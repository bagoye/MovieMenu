<template>
  <div>
    <div>
      <router-link :to="{name: 'FreeCommunityView'}">자유게시판</router-link> | 
      <router-link :to="{name: 'TogetherCommunityView'}">밥가취머거욥</router-link>
      
    </div>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'CommunityView',
}
</script>

<style>

</style>