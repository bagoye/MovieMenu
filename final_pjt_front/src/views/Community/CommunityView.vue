<template>
  <div class="community-view">
    <div class="menu-out">
      <div class="menu-in">

        <div class="category-link ">
          <router-link :to="{name: 'FreeCommunityView'}"
            exact-active-class="active-link">
            자유게시판
          </router-link>
          <router-link :to="{name: 'TogetherCommunityView'}"
            exact-active-class="active-link">
            밥가취머거욥
          </router-link>    
        </div>

        <router-view/>
      </div>
    </div>  
  </div>
</template>

<script>
export default {
  name: 'CommunityView',

}
</script>

<style>
.community-view {
  width: 100%;
  text-align: center;
}

.category-link * {
  margin-left: 40px;
  font-weight: bold;
  font-size: 16px;
  color: #000;
  text-decoration: none;
}
</style>