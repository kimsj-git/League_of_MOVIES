<template>
<div>
  <div class="container">
    <h2>최신 영화</h2>
    <div class="d-flex row row-cols-sm-2 row-cols-md-2 row-cols-lg-3 row-cols-xl-4" style="">
      <LatestMovieListItem
        v-for="latestMovie in latestMovies"
        :key="latestMovie.id"
        :latestMovie="latestMovie"/>
    </div>
  </div>
</div>
</template>

<script>
import LatestMovieListItem from '@/components/LatestMovieListItem'

export default {
  name: 'LatestMovieList',
  components: {
    LatestMovieListItem,
  },
  computed: {
    latestMovies() {
      console.log(this.$store.state.latestMovies)
      return this.$store.state.latestMovies
    }
  }
}
</script>