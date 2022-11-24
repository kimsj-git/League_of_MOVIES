<template>
  <v-container @click.stop="goMatchDetail(match.pk, match.movie_1, match.movie_2)">
    <v-row rows="auto" >
      <v-card class="row justify-content-center p-0">
        <MovieCard :movie="secMovie"/>
        <!-- <p>{{ firstMovie.title }} vs {{ secMovie.title }}</p> -->
        <MovieCard :movie="firstMovie"/>
        <!-- <v-card class="px-0 py-0 m-3" max-width="300">
          <v-img :src="firstPoster" alt="IMG" :aspect-ratio="1 / 1.414" />
        </v-card>
        <v-card class="px-0 py-0 m-3" max-width="300">
          <v-img :src="secPoster" alt="IMG" :aspect-ratio="1 / 1.414" />
        </v-card> -->
      </v-card>
      <!-- <v-col class="row justify-content-center">
      </v-col> -->
    </v-row>
  </v-container>
</template>

<script>
// import axios from 'axios'
import MovieCard from '@/components/MovieCard'

const POSTER_URL = "https://image.tmdb.org/t/p/original";
// const API_URL = 'http://127.0.0.1:8000/'

export default {
  name: "LeagueListItem",
  components: {
    MovieCard,
  },
  data() {
    return {
      firstMovie: null,
      secMovie: null,
    };
  },
  props: {
    match: Object,
  },
  computed: {
    movies() {
      return this.$store.state.movies;
    },
    firstPoster() {
      return POSTER_URL + this.firstMovie.poster_path;
    },
    secPoster() {
      return POSTER_URL + this.secMovie.poster_path;
    },
  },
  methods: {
    goMatchDetail(match_pk, movie_1, movie_2) {
      this.$router.push({
        name: "LeagueDetail",
        params: { match_pk, movie_1, movie_2 },
        props: true,
      })
    },
    getMatchMovies() {
      const firstId = this.match.movie_1;
      for (const movie of this.movies) {
        if (movie.movie_id === Number(firstId)) {
          this.firstMovie = movie;
          break;
        }
      }

      const secId = this.match.movie_2;
      for (const movie of this.movies) {
        if (movie.movie_id === Number(secId)) {
          this.secMovie = movie;
          break;
        }
      }
    },
  },
  created() {
    this.getMatchMovies();
  },
};
</script>


<style>
</style>