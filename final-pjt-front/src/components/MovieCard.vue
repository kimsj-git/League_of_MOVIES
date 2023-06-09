<template>
  <v-hover v-slot="{ hover }" open-delay="20">
    <v-card
      @click.native.stop="goDetail(movie.movie_id)"
      class="px-0 py-0 m-3 rounded-xl"
      max-width="350"
      min-width="200"
      :elevation="hover ? 16 : 2"
      :class="{ 'on-hover': hover }"
    >
      <v-img
        :src="poster"
        alt="IMG"
        :aspect-ratio="1 / 1.414"
        class="rounded-xl"
      />
      <v-btn
        @click.native.stop="movieLikes(movie.movie_id)"
        icon
        fab
        style="position: absolute; bottom: 0px; right: 0px;"
        depressed
        x-large
        class="like-btn"
      >
        <v-icon v-if="!isLiked" color="red darken-2">mdi-heart-outline</v-icon>
        <v-icon v-if="isLiked" color="red darken-2">mdi-heart</v-icon>
      </v-btn>
    </v-card>
  </v-hover>
</template>

<script>
import axios from "axios"

// const API_URL = "http://127.0.0.1:8000/";
const API_URL = "https://lom.kimsj.dev/api/v1";
const POSTER_URL = "https://image.tmdb.org/t/p/original";

export default {
  name: "MovieCard",
  data() {
    return {
      card: this.movie,
      isLiked: null,
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
    movieLikes(movie_id) {
      axios({
        method: "post",
        url: `${API_URL}api/v1/movies/${Number(movie_id)}/likes/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res);
          this.isLiked = res.data.is_liked;
          console.log(this.isLiked);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getLiked() {
      axios({
        method: "get",
        url: `${API_URL}api/v1/movies/${Number(this.movie.movie_id)}/likes/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          this.isLiked = res.data.is_liked;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  created() {
    this.getLiked();
  },
};
</script>

<style lang="sass" scoped>
.v-card.on-hover.theme--dark
  background-color: rgba(#FFF, 0.8)
  >.v-card__text
    color: #000

</style>

<style>
.like-btn::before {
  display: none;
}
</style>