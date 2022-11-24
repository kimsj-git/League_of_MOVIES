<template>
  <v-container class="my-5">
    <v-card elevation="2">
      <v-container class="text-left">
        <v-row>
          <h2>{{ movie?.title }}</h2>
          <v-col>
            <MovieCard :movie="movie" />
          </v-col>
          <v-col>
            <p>{{ movie.overview }}</p>
            <p>평점: {{ movie.vote_average }}</p>
            <p v-for="genre in movie.genres"
            :key="genre.id"
            >{{ getGenreNames(genre) }}
            </p>
            <p>{{ thisMovieGenres }}</p>
            <p></p>
          </v-col>
        </v-row>
        <p class="text-right" @click.prevent="goBack()">뒤로가기</p>
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
      thisMovieGenres: this.movie.genres,
    };
  },
  components: {
    MovieCard,
  },
  computed: {
    movies() {
      return this.$store.state.movies;
    },
    genres() {
      return this.$store.state.genres;
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
    getGenreNames(genre) {
      for (const genreList of this.genres) {
        if (genreList.id === Number(genre)) {
          this.thisMovieGenres = genreList.name;
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
    // this.getGenreNames(genre)
  },
};
</script>
  
<style>
</style>