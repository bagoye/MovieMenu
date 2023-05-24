<template>
  <div class="col-sm-6 col-md-4 col-lg-2">
    <div class="movie-card">
      <router-link
      :to="{
        name:'MovieDetailView', 
        params: { pk: movie.id }}">
        <img :src="`https://image.tmdb.org/t/p/w300_and_h450_bestv2${movie.poster_path}`">
      </router-link>

      <div class="movie-trans"></div>

      <div class="movie-card-content">
        <div class="movie-title">{{ movie.title }}</div>
        <div class="movie-btn">
          <button>▶</button>
          <button>😍</button>
        </div>
      </div>
    </div>

    
    

  </div>
</template>

<script>
export default {
  name: 'NormalMovieListItem',
  props: {
    movie: Object,
  }
}
</script>

<style>

.movie-card {
  position: relative;
  text-align: center;
  border-radius: 10px;
  overflow: hidden;
}

.movie-card-content {
  width: 100%;
  position: absolute;
  top: 30%;
  color: #fff;
  text-align: center;
  display: flex;
  flex-direction: column;
  visibility: hidden;
  transition: opacity 0.3s ease;
}

.movie-trans {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: #000;
  opacity: 60%;
  visibility: hidden;
}

.movie-card-content * {
  margin: 30px 0;
}
.movie-card:hover .movie-card-content {
  visibility: visible;
}
.movie-card:hover .movie-trans {
  visibility: visible;
}

.movie-btn * {
  margin: 0 20px;
  width: 36px;
  height: 36px;
  border: none;
  border-radius: 50%;
}

</style>