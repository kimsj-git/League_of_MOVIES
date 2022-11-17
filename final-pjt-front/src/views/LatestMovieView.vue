<template>
    <div>
    <nav>
      <router-link to="/match-ranking">리그순위</router-link> |
      <router-link to="/vote-ranking">득표순위</router-link> |
      <router-link to="/latest">최신영화</router-link>
    </nav>
    <router-view/>
    <LatestMovieList/>
  </div>
</template>

<script>
import LatestMovieList from '@/components/LatestMovieList'

export default {
  name: 'LatestMovieView',
  components: {
    LatestMovieList
  },
  created() {
    this.getLatestMovies()
  },
  methods: {
    getLatestMovies() {
      this.$store.dispatch('getLatestMovies')
    }
  }
}
</script>

<style>

</style>