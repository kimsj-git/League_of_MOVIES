<template>
<div>
  <h2>Movie League</h2>
  <v-btn @click.prevent="goMatchCreate()">
    <v-icon>mdi-fencing</v-icon>매치 만들기 <v-icon>mdi-fencing</v-icon>
  </v-btn>
  <div class="container">
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
  methods: {
    goMatchCreate() {
      this.$router.push({ name: 'CreateMatch' })
    },
  },
}
</script>