<template>
<div>
  <div class="container">
    <h2>인기 영화</h2>
    <div class="d-flex row row-cols-sm-2 row-cols-md-2 row-cols-lg-3 row-cols-xl-4" style="">
      <MovieListItem
        v-for="movie in movies"
        :key="movie.movie_id"
        :movie="movie"/>
    </div>
  </div>
</div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem'

export default {
  name: 'MovieList',
  components: {
    MovieListItem,
  },
  computed: {
    movies() {
      // console.log(this.$store.state.movies)
      return this.$store.state.movies
    }
  }
}
</script>