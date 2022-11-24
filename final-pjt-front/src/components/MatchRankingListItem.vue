<template>
  <v-container>
    <v-row>
      <v-col class="col-5">
        <h2>{{ index + 1 }}위</h2>
        <MovieCard :movie="this_movie" style="width: 200%" />
      </v-col>
      <v-col class="col-7">
        <h5>이 영화가 이긴 그저 그런 영화들</h5>
        <v-row>
          <v-col
            class="d-flex align-items-end"
            v-for="losemovie in movie.win_movies"
            :key="losemovie.movie_id"
          
          >
            <img
              :src="
                'https://image.tmdb.org/t/p/original' + losemovie.poster_path
              "
              alt="IMG"
              style="width: auto; height: 250px"
              class="rounded-xl"
              @click.native.stop="goDetail(losemovie.movie_id)"
            />
          </v-col>
        </v-row>

        <!-- <MovieCard 
              v-for="losemovie in movie.win_movies"
              :key="losemovie.movie_id"
              :movie="losemovie" 
            /> -->
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
import MovieCard from "@/components/MovieCard";

const POSTER_URL = "https://image.tmdb.org/t/p/original";
const API_URL = "http://127.0.0.1:8000/";

export default {
  name: "MatchRankingListItem",
  components: {
    MovieCard,
  },
  data() {
    return {
      isLiked: null,
      loseMovies: [],
      this_movie: this.movie,
    };
  },
  props: {
    index: Number,
    movie: Object,
  },
  created() {
    this.getLiked();
    // this.getLoseMovies()
  },
  computed: {
    movieData() {
      return this.$store.state.movies;
    },
    posterMain() {
      //  console.log(this.movie.pk)
      return POSTER_URL + this.movie.poster_path;
    },
    // posterLose() {
    //   //  console.log(this.movie.pk)
    //   let loseMovie = this.loseMovie
    //   return POSTER_URL + loseMovie.poster_path
    // },
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
    // getLoseMovies() {
    //   for (const loseMovie of this.movie.win_movies) {
    //     this.getMovieName(loseMovie)
    //   }
    // },
    // getMovieName(loseMovie) {
    //   let id = loseMovie
    //   for (const movie of this.movieData) {
    //     if (movie.movie_id === Number(id)) {
    //       this.loseMovies.push = movie
    //       break
    //     }
    //   }
    // },
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