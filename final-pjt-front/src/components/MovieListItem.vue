<template>
  <v-card
    @click.stop="goDetail(movie.movie_id)"
    class="px-0 py-0"
    max-width="400"
  >
    <v-img :src="poster" alt="IMG" :aspect-ratio="1 / 1.414" />
  </v-card>
  <!-- <div @click.stop="goDetail(movie.movie_id)">
    <div class="flip-card">
      <div class="flip-card-inner">
        <div class="flip-card-front">
          <img :src="poster" alt="IMG" style="width:100%;height:100%;">
        </div>
        <div class="flip-card-back">
          <h3>{{ movie.title }}</h3>
          <p>{{ movie.overview }}</p>
          <button v-if="isLiked" @click.stop="movieLikes(movie.movie_id)">좋아요 취소</button>
          <button v-if="!isLiked" @click.stop="movieLikes(movie.movie_id)">좋아요</button>
        </div>
      </div>
    </div>

  </div> -->
</template>

<script>
import axios from "axios";

const POSTER_URL = "https://image.tmdb.org/t/p/original";
const API_URL = "http://127.0.0.1:8000/";

export default {
  name: "MovieListItem",
  components: {},
  data() {
    return {
      isLiked: null,
    };
  },
  props: {
    movie: Object,
  },
  created() {
    this.getLiked();
  },
  methods: {
    goDetail(movie_id) {
      this.$router.push({ name: "MovieDetail", params: { movie_id } });
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
  },
  computed: {
    poster() {
      //  console.log(this.movie.pk)
      return POSTER_URL + this.movie.poster_path;
    },
  },
};
</script>


<style>
/* The flip card container - set the width and height to whatever you want. We have added the border property to demonstrate that the flip itself goes out of the box on hover (remove perspective if you don't want the 3D effect */
.flip-card {
  background-color: transparent;
  width: 300px;
  height: 400px;
  border: 1px solid #f1f1f1;
  perspective: 1000px; /* Remove this if you don't want the 3D effect */
}

/* This container is needed to position the front and back side */
.flip-card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  text-align: center;
  transition: transform 0.8s;
  transform-style: preserve-3d;
}

/* Do an horizontal flip when you move the mouse over the flip box container */
.flip-card:hover .flip-card-inner {
  transform: rotateY(180deg);
}

/* Position the front and back side */
.flip-card-front,
.flip-card-back {
  position: absolute;
  width: 100%;
  height: 100%;
  -webkit-backface-visibility: hidden; /* Safari */
  backface-visibility: hidden;
}

/* Style the front side (fallback if image is missing) */
.flip-card-front {
  background-color: #bbb;
  color: black;
}

/* Style the back side */
.flip-card-back {
  background-color: beige;
  color: black;
  transform: rotateY(180deg);
}
</style>