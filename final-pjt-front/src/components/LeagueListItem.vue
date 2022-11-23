<template>
  <div @click.stop="goMatchDetail(match.pk, match.movie_1, match.movie_2)">
    <!-- <h4>{{ match }}</h4> -->
    <br />
    <img :src="firstPoster" alt="IMG" style="width: 30%; height: 43%" />
    <img :src="secPoster" alt="IMG" style="width: 30%; height: 43%" />
    <br />
    <h4>{{ firstMovie.title }} vs {{ secMovie.title }}</h4>
    <hr />
  </div>
</template>

<script>
// import axios from 'axios'

const POSTER_URL = "https://image.tmdb.org/t/p/original";
// const API_URL = 'http://127.0.0.1:8000/'

export default {
  name: "LeagueListItem",
  components: {},
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
      });
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