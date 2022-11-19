<template>
  <div class="home">
    <nav>
      <router-link to="/match-ranking">리그순위</router-link> |
      <router-link to="/vote-ranking">득표순위</router-link> |
      <router-link to="/latest">최신영화</router-link>
    </nav>
    <router-view/>
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
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  created() {
    this.getMovies()
  },
  methods: {
    getMovies() {
      if (this.isLogin === true) {
        this.$store.dispatch('getMovies')
      } else {
        alert('여기서 로그인하셔야 합니다.')
        this.$router.push({ name: 'LogInView' })
      }
    }
  }
}
</script>
