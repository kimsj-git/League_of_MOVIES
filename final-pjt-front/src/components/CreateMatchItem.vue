<template>
  <v-card class="p-0" @click.prevent="userSelected">
    <v-img :src="poster" alt="IMG" :aspect-ratio="1 / 1.414" />
    <p>{{ movie.title }}</p>
  </v-card>
</template>

<script>
const POSTER_URL = "https://image.tmdb.org/t/p/original";

export default {
  name: "CreateMatchItem",
  props: {
    movie: Object,
  },
  computed: {
    poster() {
      //  console.log(this.movie.pk)
      return POSTER_URL + this.movie.poster_path;
    },
  },
  methods: {
    userSelected : function() {
    let selectedMovie = this.movie
    this.$emit('select-match-movie', selectedMovie)
  },
  }
};
</script>

<style>

</style>