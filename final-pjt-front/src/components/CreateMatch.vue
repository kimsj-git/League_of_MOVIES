<template>
  <div>
    <h2>매치를 생성하세요</h2>
    <!-- 2개 선택 후 submit하면 요청 보내기 -->
    <form @submit.prevent="createMatch" class="row justify-content-around">
      <div id="select-movie">
        <img src="" alt="movie1">
      </div>
      <div id="select-movie">
        <img src="" alt="movie2">
      </div>
      <input type="submit" value="매치 시작!">
    </form>

    <!-- 카드리스트에서 영화 두개 선택 -->
    <v-container flex>
      <v-row rows=auto>
        <v-col class="row p-0 justify-content-center">
          <CreateMatchItem
          @click.prevent="getMatchMovies"
          class="m-2"
          :class="grid-selected-movie"
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
    }
  },
  computed: {
    movieDataBase() {
      return this.$store.state.movies
    }
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
  },
  } 
</script>

<style>
#select-movie{
  width: 30%;
  height: 20rem;
  border: solid black;
}

#grid-selected-movie{
  border: solid gold;
}
</style>