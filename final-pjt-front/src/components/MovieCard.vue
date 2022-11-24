<template>
  <v-hover v-slot="{ hover }" open-delay="20">
    <v-card
      @click.stop="goDetail(movie.movie_id)"
      class="px-0 py-0 m-3 rounded-xl"
      max-width="350"
      min-width="200"
      :elevation="hover ? 16 : 2"
      :class="{ 'on-hover': hover }"
    >
      <v-img :src="poster" alt="IMG" :aspect-ratio="1 / 1.414" />
    </v-card>
  </v-hover>
</template>

<script>
const POSTER_URL = "https://image.tmdb.org/t/p/original";

export default {
  name: "MovieCard",
  data() {
    return {
      card: this.movie,
    };
  },
  props: {
    movie: Object,
  },
  computed: {
    movies() {
      return this.$store.state.movies;
    },
    poster() {
      return POSTER_URL + this.card.poster_path;
    },
  },
  methods: {
    goDetail(movie_id) {
      this.$router.push({ name: "MovieDetail", params: { movie_id } });
    },
  },
};
</script>

<style lang="sass" scoped>
.v-card.on-hover.theme--dark
  background-color: rgba(#FFF, 0.8)
  >.v-card__text
    color: #000
</style>