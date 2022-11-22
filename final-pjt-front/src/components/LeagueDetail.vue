<template>
    <div>      
      <h2>Match Detail</h2>
      <img @click.stop="goDetail(firstMovie.movie_id)" :src="firstPoster" alt="IMG" style="width:40%;height:auto;">
      <img @click.stop="goDetail(secMovie.movie_id)" :src="secPoster" alt="IMG" style="width:40%;height:auto;">  
      <p>{{ firstMovie.title }} vs {{ secMovie.title }}</p>
      <hr>
      <h5>투표수</h5>
      <p>{{ match?.movie_1_voters.length }} : {{ match?.movie_2_voters.length }}</p>
      <hr>
      <h5>댓글</h5>
      <p>{{ comments.length }}개의 댓글이 있습니다.</p>

      <form @submit.prevent="createComment">
        <label for="content">댓글: </label>
        <textarea v-model="content" id="content" cols="30" rows="3"></textarea>
        <input type="submit" value="작성">
      </form>

      <LeagueDetailComments
        v-for="comment in comments"
        :key="comment.id"
        :comment="comment"/>
      <p @click.prevent="goBack()">뒤로가기</p>
    </div>
  </template>
  
<script>
import LeagueDetailComments from '@/components/LeagueDetailComments'
import axios from 'axios'

const POSTER_URL = 'https://image.tmdb.org/t/p/original'
const MATCH_URL = 'http://127.0.0.1:8000/api/v1/league'


export default {
  name: 'LeagueDetail',
  components: {
    LeagueDetailComments
  },
  props: {
    match_pk: String,
    movie_1: String,
    movie_2: String,
  },
  data() {
    return {
      firstMovie: null,
      secMovie: null,
      match: null,
      comments: null,
      content: null,
    }
  },
  computed: {
    movies() {
        return this.$store.state.movies
    },
    firstPoster() {
        return POSTER_URL + this.firstMovie.poster_path
    },
    secPoster() {
        return POSTER_URL + this.secMovie.poster_path
    },
  },
  methods: {
    getMatchDetail() {
      const match_pk = this.$route.params.match_pk
      axios({
        method:'get',
        url: `${MATCH_URL}/${match_pk}`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        }
      })
        .then((res) => {
          this.match = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getMatchMovies() {
        const firstId = this.$route.params.movie_1
        for (const movie of this.movies) {
            if (movie.movie_id === Number(firstId)) {
                this.firstMovie = movie
                break
            }
        }

        const secId = this.$route.params.movie_2
        for (const movie of this.movies) {
            if (movie.movie_id === Number(secId)) {
                this.secMovie = movie
                break
            }
        }
    },
    getComments() {
      axios({
        method:'get',
        url: `${MATCH_URL}/${Number(this.$route.params.match_pk)}/comments/`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        }
      })
        .then((res) => {
          this.comments = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    goDetail(movie_id) {
      this.$router.push({ name: 'MovieDetail', params:{movie_id} })
    },
    goBack() {
      this.$router.go(-1)
    },
    createComment() {
      let content = this.content
      axios({
        method:'post',
        url: `${MATCH_URL}/${Number(this.$route.params.match_pk)}/comments/`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        },
        data: { content }
      })
        .then(() => {
          this.getComments()
          this.content = ''
        })
        .catch((err) => {
          console.log(err)
        })
    },
    saveParamsToSessionStorage() {
      const match_pk = this.match_pk
      this.$store.dispatch('saveParamsToSessionStorage', match_pk)
    }

  },
  created() {
    this.getMatchDetail()
    this.getMatchMovies()
    this.getComments()
    this.saveParamsToSessionStorage()
  },
  mounted() {
    this.paramsData.match_pk = this.$route.params.match_pk,
    this.paramsData.movie_1 = this.$route.params.movie_1,
    this.paramsData.movie_2 = this.$route.params.movie_2
  }
}


</script>


<style>

</style>