<template>
  <div>
    <nav>
      <router-link to="/match-ranking">리그순위</router-link> |
      <router-link to="/vote-ranking">득표순위</router-link> |
      <router-link to="/latest">최신영화</router-link>
    </nav>
    <router-view/>
    <VoteRankingList/>
  </div>
</template>

<script>

import VoteRankingList from '@/components/VoteRankingList'

export default {
  name: 'MatchRankingView',
  components: {
    VoteRankingList
  }
}
</script>

<style>

</style>