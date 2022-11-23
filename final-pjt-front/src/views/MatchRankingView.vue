<template>
  <div>
    <nav>
      <router-link to="/match-ranking">리그순위</router-link> |
      <router-link to="/vote-ranking">득표순위</router-link> |
      <router-link to="/latest">최신영화</router-link>
    </nav>
    <router-view/>
    <MatchRankingList/>
  </div>
</template>

<script>

import MatchRankingList from '@/components/MatchRankingList'

export default {
  name: 'MatchRankingView',
  components: {
    MatchRankingList
  }
}
</script>

<style>

</style>