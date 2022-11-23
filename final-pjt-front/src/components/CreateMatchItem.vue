<template>
      <v-card class="px-0 py-0">
      <v-img :src="poster" alt="IMG" :aspect-ratio="1/1.414"/>
      </v-card>
</template>

<script>
const POSTER_URL = 'https://image.tmdb.org/t/p/original'

export default {
  name: 'CreateMatchItem',
  props: {
    movie: Object, 
  },
  computed: {
    poster() {
      //  console.log(this.movie.pk)
      return POSTER_URL + this.movie.poster_path
    }, 
  }
}
</script>

<style>

</style>