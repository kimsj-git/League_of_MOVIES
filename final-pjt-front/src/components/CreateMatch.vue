<template>
  <div>
    <h2>매치를 생성하세요</h2>
    <!-- 2개 선택 후 submit하면 요청 보내기 -->
    <form @submit.prevent="createMatch" class="row justify-content-around">
      <div id="select-movie">
        <img v-if="firstMovie" :src="firstPoster" alt="movie1" style="width: 100%; height: 100%; object-fit:scale-down;">
      </div>
      <div id="select-movie">
        <img v-if="secMovie" :src="secPoster" alt="movie2" style="width: 100%; height: 100%; object-fit:scale-down;">
      </div>
      <input type="submit" value="매치 시작!">
    </form>

    <!-- 카드리스트에서 영화 두개 선택 -->
    <v-container flex>
      <v-row rows=auto>
        <v-col class="row p-0 justify-content-center">
          <CreateMatchItem
          @select-match-movie="selectMatchMovie"
          class="m-2"
          style="width: 10rem;"
          v-for="movie in movieDataBase"
          :key="movie.movie_id"
          :movie="movie"/>
        </v-col>
      </v-row>
    </v-container>


  </div>
</template>

<script>
import CreateMatchItem from '@/components/CreateMatchItem'
import axios from 'axios';

const POSTER_URL = "https://image.tmdb.org/t/p/original";
const MATCH_URL = 'http://127.0.0.1:8000/api/v1/league/'

export default {
  name: 'CreateMatch',
  components: {
    CreateMatchItem
  },
  data () {
    return {
      firstMovie: null,
      secMovie: null,
      movies: null,
      isSelected: false,
    }
  },
  computed: {
    movieDataBase() {
      return this.$store.state.movies
    },
    // newMatchPk() {
    //   const matchDB = this.$store.state.matches
    //   const latestIndex = this.$store.state.matches.length - 1
    //   return matchDB[latestIndex].pk + 1;
    // },
    firstPoster() {
      //  console.log(this.movie.pk)
      return POSTER_URL + this.firstMovie.poster_path;
    },
    secPoster() {
      //  console.log(this.movie.pk)
      return POSTER_URL + this.secMovie.poster_path;
    },
  },
  methods: {
    getMatchMovies() {
      const firstId = this.match.movie_1;
      for (const movie of this.movieDataBase) {
        if (movie.movie_id === Number(firstId)) {
          this.firstMovie = movie;
          break;
        }
      }

      const secId = this.match.movie_2;
      for (const movie of this.movieDataBase) {
        if (movie.movie_id === Number(secId)) {
          this.secMovie = movie;
          break;
        }
      }
    },
    selectMatchMovie(selectedMovie) {
      console.log(selectedMovie)
      this.isSelected = !this.isSelected
      console.log(this.isSelected)
      if ((this.firstMovie === null) && (this.secMovie !== selectedMovie)) {
        this.firstMovie = selectedMovie
      } else if (this.firstMovie === selectedMovie) {
        // alert('같은 영화는 선택할 수 없어!')
        this.firstMovie = null
      }else if ((this.firstMovie !== null) && (this.secMovie === null)) {
        this.secMovie = selectedMovie
      } else if (this.secMovie === selectedMovie) {
        this.secMovie = null
      } else if ((this.firstMovie !== null) && (this.secMovie !== null)) {
        alert('영화를 모두 선택했습니다')
      }
    },
    createMatch() {
      if ((this.firstMovie !== null) && (this.secMovie !== null)) {
        //매치생성 axios
        const movie_1 = this.firstMovie.movie_id
        const movie_2 = this.secMovie.movie_id
        axios({
          method:'post',
          url: `${MATCH_URL}`,
          data: {
            // views.py에서 user.pk값이 자동으로 안들어가는거 고쳐야함
            "user": 1,
            "movie_1": movie_1,
            "movie_2": movie_2, 
          },
          headers: {
          Authorization: `Token ${ this.$store.state.token }`
        }
        })
          .then((res) => {
            const newMatchPk = res.data.id
            // 생성된 match detail페이지 라우팅
            this.$router.push({ 
              path: `/league/${Number(newMatchPk)}`, 
              params: { newMatchPk, movie_1, movie_2, }, 
              props: true, }),
            console.log(newMatchPk)
            console.log(movie_1)
            console.log(movie_2)
            // this.$router.push({ name: 'LeagueView' })
          })
          .catch((err) => {
            console.log(err)
          })
      } else {
        alert('영화를 두 개 선택해주세요')
      }
    }
  },
  } 
</script>

<style>
#select-movie{
  width: 30%;
  height: 20rem;
  border: solid black;
}

.grid-selected-movie{
  border: solid gold;
}
</style>