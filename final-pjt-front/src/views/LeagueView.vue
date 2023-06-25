<template>
  <div class="league">
    <router-view/>
    <LeagueList/>
  </div>
</template>

<script>
// @ is an alias to /src
import LeagueList from '@/components/LeagueList'

export default {
  name: 'LeagueView',
  components: {
    LeagueList,
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  created() {
    this.getMatches()
  },
  methods: {
    getMatches() {
      if (this.isLogin === true) {
        this.$store.dispatch('getMovies')
        this.$store.dispatch('getGenres')
        this.$store.dispatch('getMatches')
      } else {
        alert('여기서 로그인하셔야 합니다.')
        this.$router.push({ name: 'LogInView' })
      }
    }
  }
}
</script>