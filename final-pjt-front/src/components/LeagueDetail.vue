<template>
    <v-container>     
      <h3>{{ firstMovie.title }} VS {{ secMovie.title }}</h3>
      <v-row>
        <v-col>
          <img @click.stop="goDetail(firstMovie.movie_id, match_pk)" :src="firstPoster" alt="IMG" style="width:40%;height:auto;">
          <img @click.stop="goDetail(secMovie.movie_id, match_pk)" :src="secPoster" alt="IMG" style="width:40%;height:auto;">  
          <div class="d-flex justify-content-center">
            <div>
              <label for="movie1">{{ firstMovie.title }}</label>
              <br>
              <input @click="voteMovie(firstMovie.movie_id)" id="movie1" type="radio" name="selectMovie">
            </div>
            <p>  VS  </p>
            <div>
              <label for="movie2">{{ secMovie.title }}</label>
              <br>
              <input @click="voteMovie(secMovie.movie_id)" id="movie2" type="radio" name="selectMovie">
            </div>
          </div>
          <br>
            <button @click="goVotes">투표하기</button>
          <hr>
          <h5>투표수</h5>
          <p>{{ match.movie_1_voters?.length }} : {{ this.match.movie_2_voters?.length }}</p>
          <hr>
        </v-col>
        
        <v-col>
          <h5>댓글</h5>
          <p>{{ comments.length }}개의 댓글이 있습니다.</p>

          <form @submit.prevent="createComment">
            <label for="content">댓글: </label>
            <v-textarea outlined v-model="content" id="content" cols="30" rows="3" label="여기에 댓글 다셔야 합니다."></v-textarea>
            <input type="submit" value="작성">
          </form>

          <LeagueDetailComments
            v-for="comment in comments"
            :key="comment.id"
            :comment="comment"
            @delete-comment="deleteComment"
            @modify-comment="modifyComment"/>
          <p @click.prevent="goBack()">뒤로가기</p>
        </v-col>
      </v-row>
    </v-container>
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
      selectMoviePk: null,
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
    // firstMovieVotersCount() {
    //   if (this.match.movie_1_voters) {
    //     return this.match.movie_1_voters.length
    //   }
    // },
    // secMovieVotersCount() {
    //   return this.match?.movie_2_voters?.length
    // },
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
    goDetail(movie_id, match_pk) {
      this.$router.push({ name: 'LeagueMovieDetail', params:{match_pk, movie_id}, props: true })
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
    modifyComment(commentId, modifyContent) {
      axios({
        method:'put',
        url: `${MATCH_URL}/${Number(this.$route.params.match_pk)}/comments/${commentId}/`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        },
        data: { "content" : modifyContent }
      })
        .then(() => {
          this.getComments()
        })
        .catch((err) => {
          console.log(err)
        })
    },
		deleteComment(commentId) {
		axios({
			method:'delete',
			url: `${MATCH_URL}/${Number(this.$route.params.match_pk)}/comments/${commentId}/`,
			headers: {
			Authorization: `Token ${ this.$store.state.token }`
			},
		})
			.then(() => {
        this.getComments()
			})
			.catch((err) => {
			console.log(err)
			})
		},

    voteMovie(movie_pk) {
      if (movie_pk === this.firstMovie.movie_pk) {
        this.selectMoviePk = movie_pk
      } else {
        this.selectMoviePk = movie_pk
      }
    },
    goVotes() {
      axios({
        method: 'post',
        url: `${MATCH_URL}/${Number(this.$route.params.match_pk)}/${this.selectMoviePk}/`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        }
      })
        .then((res) => {
          if (res.status === 208) {
            alert('͡° ͜ʖ ͡°,,,,,그대는 이미 투표에 참여했어')
          } else (
            this.getMatchDetail()
          )
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  created() {
    this.getMatchDetail()
    this.getMatchMovies()
    this.getComments()
  },
}


</script>


<style>

</style>