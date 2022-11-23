<template>
  <div class="my-5">
    <v-card class="row justify-content-center">

      <v-card-text id="powerDown">
        <v-subheader class="pa-0">
          첫 번째 영화 검색
        </v-subheader>
        <v-autocomplete
          v-model="first_movie"
          :items="movies"
        >
        </v-autocomplete>
      </v-card-text>

      <v-card-text id="powerDown">
        <v-subheader class="pa-0">
          두 번째 영화 검색
        </v-subheader>
        <v-autocomplete
          v-model="secon_movie"
          :items="movieDataBase"
        >
        </v-autocomplete>
      </v-card-text>
    </v-card>

  <h2 class="my-5">매치를 생성하세요</h2>
  <form @submit.prevent="createMatch">
    <!-- 서치 바에서 입력 -->

    <!-- 입력에 따라서 DB에서 검색한 영화들 표시, 2개 선택 -->

    <!-- 2개 선택 후 submit하면 요청 보내기 -->
    <input type="submit" value="매치 시작!">
  </form>
  </div>
</template>

<script>
export default {
  name: 'CreateMatch',
  data () {
    return {
      first_movie: null,
      secon_movie: null,
      movies: null,
    }
  },
  created() {
    movieDataBase()
  },
  computed: {
    movieDataBase() {
      console.log(this.$store.state.movies)
      return this.$store.state.movies
    }
  },
  } 
</script>

<style>
#powerDown {
  width: 40%;
}


</style>