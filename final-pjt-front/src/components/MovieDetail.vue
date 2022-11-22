<template>
    <div>
      <h2>Movie Detail: {{movie?.title}}</h2>
      <img :src="poster" alt="IMG" style="width:40%;height:auto;"> 
      <p>{{ movie.overview }}</p>
      <p @click.prevent="goBack()">뒤로가기</p>
    </div>
  </template>
  
  <script>

  const POSTER_URL = 'https://image.tmdb.org/t/p/original'

  export default {
    name: 'MovieDetail',
    data() {
      return {
        movie: null
      }
    },
    computed: {
      movies() {
        return this.$store.state.movies
      },
      poster() {
      return POSTER_URL + this.movie.poster_path
     }
    },
    methods: {
      getMovieId() {
        const id = this.$route.params.movie_id
        for (const movie of this.movies) {
          if (movie.movie_id === Number(id)) {
            this.movie = movie
            break
          }
        }
      },
      goBack() {
        this.$router.go(-1)
      },
    },
    created() {
      this.getMovieId(this.$route.params.id)
    }
  }
  </script>
  
  <style>
  
  </style>