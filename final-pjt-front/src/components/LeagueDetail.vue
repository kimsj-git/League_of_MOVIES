<template>
    <div>
      <h2>Match Detail</h2>
      <img :src="firstPoster" alt="IMG" style="width:40%;height:auto;">
      <img :src="secPoster" alt="IMG" style="width:40%;height:auto;">  
      <p>{{ firstMovie.title }} vs {{ secMovie.title }}</p>

      <router-link :to="{ name: 'LeagueView' }">뒤로가기</router-link>
    </div>
  </template>
  
<script>

const POSTER_URL = 'https://image.tmdb.org/t/p/original'

export default {
  name: 'LeagueDetail',
  components: {
  },
  data() {
    return {
      firstMovie: null,
      secMovie: null,
    }
  },
  computed: {
    movies() {
        return this.$store.state.movies
    },
    firstPoster() {
        return POSTER_URL + this.firstMovie.poster_path
    },
    secPoster() {
        return POSTER_URL + this.secMovie.poster_path
    },
  },
  methods: {
    getMatchMovies() {
        const firstId = this.$route.params.movie_1
        for (const movie of this.movies) {
            if (movie.movie_id === Number(firstId)) {
                this.firstMovie = movie
                break
            }
        }

        const secId = this.$route.params.movie_2
        for (const movie of this.movies) {
            if (movie.movie_id === Number(secId)) {
                this.secMovie = movie
                break
            }
        }
    }
  },
  created() {
    this.getMatchMovies()
  }
}
</script>


<style>

</style>