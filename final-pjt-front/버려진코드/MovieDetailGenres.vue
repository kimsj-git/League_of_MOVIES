<template>
<div>
    <p>{{ genre }}</p>
    <p>{{ genres }}</p>
    <!-- <p>{{ movies }}</p> -->
</div>
</template> 
  
<script>

export default {
name: "MovieDetailGenres",
props: {
    genre: String,
},
data() {
    return{
        genreName: null,
    }
},
computed: {
    movies() {
    // console.log(this.$store.state.movies)
    return this.$store.state.movies;
    },
    genres() {
      return this.$store.state.genres;
    }
    
},
methods: {
    getGenreName() {
        const Id = this.genre
        for (const genre of this.genres) {
        if (genre.id === Number(Id)) {
          this.genreName = genre;
          break;
        }
      }
    },
    },
created() {
    this.getGenreName()
}
}
</script>