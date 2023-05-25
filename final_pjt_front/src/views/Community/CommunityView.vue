<template>
  <div class="community-view">
    <div class="menu-out">
      <div class="menu-in">

        <div class="category-link mt-5 mx-auto row">
          <router-link :to="{name: 'FreeCommunityView'}"
            exact-active-class="active-link" class="col-6">
            자유 게시판
          </router-link>
          <router-link :to="{name: 'TogetherCommunityView'}"
            exact-active-class="active-link" class="col-6">
            영화 같이 봐요
          </router-link>    
        </div>

        <router-view class="mt-5"/>
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
.category-link {
  width: 60%;
}

.category-link * {
  text-align: center;
  font-weight: bold;
  font-size: 16px;
  color: #000;
  text-decoration: none;
}
.category-link *:hover {
  color: #2E8ADF;
}

.active-link {
  color: #2E8ADF;
}
</style>