<template>
    <div>
      <h2>Movie Detail 페이지</h2>
      <p>{{ movie.title }}</p>  
      <p>{{ movie.overview }}</p>

    </div>
  </template>
  
  <script>
  export default {
    name: 'MovieDetail',
    props: {
        movie: Object,
    },
  }
  </script>
  
  <style>
  
  </style>