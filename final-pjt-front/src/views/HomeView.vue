<template>
  <div class="home">
    <MovieList/>
  </div>
</template>

<script>
// @ is an alias to /src
import MovieList from '@/components/MovieList'

export default {
  name: 'HomeView',
  components: {
    MovieList,
  },
  created() {
    this.getMovies()
  },
  methods: {
    getMovies() {
      this.$store.dispatch('getMovies')
    }
  }
}
</script>
