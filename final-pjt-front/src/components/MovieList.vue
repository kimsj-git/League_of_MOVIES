<template>
  <v-container flex>
    <h2>인기 영화</h2>
    <v-row rows="auto">
      <v-col class="row justify-content-center">
        <MovieListItem
          v-for="movie in movies"
          :key="movie.movie_id"
          :movie="movie"
          class="m-2"
          style="width: 15rem;"
        />
      </v-col>
    </v-row>
  </v-container>
</template> 

<script>
import MovieListItem from "@/components/MovieListItem";

export default {
  name: "MovieList",
  components: {
    MovieListItem,
  },
  computed: {
    movies() {
      // console.log(this.$store.state.movies)
      return this.$store.state.movies;
    },
  },
};
</script>