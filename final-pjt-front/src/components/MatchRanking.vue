<template>
    <div>
    <nav>
      <router-link to="/match-ranking">리그순위</router-link> |
      <router-link to="/vote-ranking">득표순위</router-link> |
      <router-link to="/latest">최신영화</router-link>
    </nav>
    <router-view/>
    <h1>리그순위</h1>
  </div>
</template>

<script>
export default {
  name: 'MatchRanking'
}
</script>

<style>

</style>