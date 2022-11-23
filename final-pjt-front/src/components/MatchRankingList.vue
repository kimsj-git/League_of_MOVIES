<template>
  <div>
    <h2>Match Ranking</h2>
    <!-- <button @click.prevent="goMatchCreate()">매치 만들기!</button> -->
    <div class="container">
      <!-- <CreateMatch/> -->
      <hr>
      <div>
        <MatchRankingListItem
            v-for="(movie, index) in rankingMovies"
            :key="movie.movie_id"
            :index="index"
            :movie="movie"/>
      </div>
    </div>
  </div>
</template>

<script>
import MatchRankingListItem from '@/components/MatchRankingListItem'
import axios from 'axios'

// const POSTER_URL = 'https://image.tmdb.org/t/p/original'
const API_URL = 'http://127.0.0.1:8000/api/v1'

export default {
  name: 'MatchRankingList',
  components: {
    MatchRankingListItem
  },
  data() {
    return {
      rankingMovies: null,
    }
  },
  computed: {
    },
  methods: {
    moviesRanking() {
      axios({
        method: 'get',
        url: `${API_URL}/ranking/win_rate/`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        },
      })
        .then((res) => {
          // console.log(res)
          this.rankingMovies = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    goMatchCreate() {
      this.$router.push({ name: 'CreateMatch' })
    },
  },
  created() {
    this.moviesRanking()
  }

}
</script>