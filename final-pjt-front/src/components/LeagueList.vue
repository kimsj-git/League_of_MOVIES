<template>
<div>
  <div class="container">
    <h2>Movie League</h2>
    <button @click="goMatchCreate">매치 만들기!</button>
    <!-- <CreateMatch/> -->
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
// import CreateMatch from '@/components/CreateMatch'

export default {
  name: 'LeagueList',
  components: {
    LeagueListItem,
    // CreateMatch,
  },
  computed: {
    matches() {
      // console.log(this.$store.state.movies)
      return this.$store.state.matches
    }
  },
  method: {
    goMatchCreate() {

      console.log('클릭했음!!')
      this.$router.push({ name: 'CreateMatch' })
    },
  },
}
</script>