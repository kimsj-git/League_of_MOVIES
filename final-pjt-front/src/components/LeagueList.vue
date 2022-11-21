<template>
<div>
  <div class="container">
    <h2>Movie League</h2>
    <hr>
    <div>
      <LeagueListItem
        v-for="match in matches"
        :key="match.id"
        :match="match"/>
    </div>
  </div>
</div>
</template>

<script>
import LeagueListItem from '@/components/LeagueListItem'

export default {
  name: 'LeagueList',
  components: {
    LeagueListItem,
  },
  computed: {
    matches() {
      // console.log(this.$store.state.movies)
      return this.$store.state.matches
    }
  }
}
</script>