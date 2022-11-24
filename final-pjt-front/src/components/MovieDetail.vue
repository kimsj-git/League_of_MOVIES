<template>
  <v-container>
    <v-card elevation="2">
      <v-container>
        <v-row>
          <h2>{{ movie?.title }}</h2>
          <v-col>
            <MovieCard :movie="movie" />
          </v-col>
          <v-col>
            <p>{{ movie.overview }}</p>
            <p>{{ movie.vote_average }}</p>
            <p>{{ movie.genres }}</p>
            <p></p>
          </v-col>
        </v-row>
        <p @click.prevent="goBack()">뒤로가기</p>
      </v-container>
    </v-card>
  </v-container>
</template>
  
<script>
import MovieCard from '@/components/MovieCard'
const POSTER_URL = "https://image.tmdb.org/t/p/original";

export default {
  name: "MovieDetail",
  data() {
    return {
      movie: null,
    };
  },
  components: {
    MovieCard,
  },
  computed: {
    movies() {
      return this.$store.state.movies;
    },
    poster() {
      return POSTER_URL + this.movie.poster_path;
    },
  },
  methods: {
    getMovieId() {
      const id = this.$route.params.movie_id;
      for (const movie of this.movies) {
        if (movie.movie_id === Number(id)) {
          this.movie = movie;
          break;
        }
      }
    },
    goBack() {
      this.$router.go(-1);
    },
  },
  created() {
    this.getMovieId(this.$route.params.id);
  },
};
</script>
  
<style>
</style>