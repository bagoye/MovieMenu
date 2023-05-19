<template>
  <div>
    <h1>Detail</h1>
    <iframe width="560" height="315" :src="`https://www.youtube.com/embed/${movie?.youtube_key}`" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    <p>제목 : {{ movie?.title }}</p>
    <p>평점 : {{ movie?.vote_average }}</p>
    <p>러닝타임 : {{ movie?.runtime }}</p>
    <p>감독 : 
      <img :src="`https://image.tmdb.org/t/p/w300_and_h450_bestv2${movie?.directors[0].profile_path}`" style="width: 100px;">
      {{ movie?.directors[0].name }}
    </p>
    <!-- <p>배우 : {{ movie?.actors }}</p> -->
    <p>배우:</p>
      <div v-for="(actor, index) in movie?.actors" :key="index">
        <img :src="`https://image.tmdb.org/t/p/w300_and_h450_bestv2${actor.profile_path}`" style="width: 100px;">
        {{ actor.name }}
      </div>
    <p>줄거리: {{ movie?.overview }} </p>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'MovieDetailView',
  data() {
    return {
      movie: null,
      actors: null,
      directors: null
    }
  },
  created() {
    this.getMovieDetail()
  },
  methods: {
    getMovieDetail() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/${this.$route.params.pk}/`
      })
      .then((res) => {
        console.log(res)
        this.movie = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
}
</script>
