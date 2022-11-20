<template>
  <div>
    <div class="flip-card">
      <div class="flip-card-inner">
        <div class="flip-card-front">
          <img :src="poster" alt="IMG" style="width:100%;height:100%;">
        </div>
        <div class="flip-card-back">
          <h3>{{ movie.title }}</h3>
          <p>{{ movie.movie_id }}</p>
          <p>{{ movie.overview }}</p>
          <!-- <MovieDetail/> -->
        </div>
      </div>
    </div>

  </div>
</template>

<script>

// import MovieDetail from '@/components/MovieDetail'

const POSTER_URL = 'https://image.tmdb.org/t/p/original'

export default {
  name: 'MovieListItem',
  components: {
    // MovieDetail
  },
  props: {
    movie: Object,
  },
  computed: {
     poster() {
       console.log(this.movie.pk)
      return POSTER_URL + this.movie.poster_path
     } 

  }
}
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
.flip-card-front, .flip-card-back {
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