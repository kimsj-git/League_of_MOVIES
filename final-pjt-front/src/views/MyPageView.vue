<template>
  <div class="mypage">
    <br>
    <v-card
      max-width="70%"
      class="mx-auto"
    >

    <v-img
    height="200px"
    src="https://mblogthumb-phinf.pstatic.net/MjAxNzA4MjhfMTAx/MDAxNTAzOTI1NDI1ODc3.xVi6dquVjmUZ4sBoE_2mlr7hJgPsYGB2iw1FuVOgxzEg.CRM4Z0yvH3WjMdhcX7u_gDXlhHductmu61vBiWDu9Aog.JPEG.imurmvp/%EC%9D%B4%ED%8B%B0.jpg?type=w800"
  >
    <v-app-bar
      flat
      color="rgba(0, 0, 0, 0)"
    >
 

      <v-spacer></v-spacer>

    </v-app-bar>

    <v-card-title class="white--text mt-8">
      <v-avatar size="56">
        <img
          alt="user"
          src="https://cloudfront-ap-northeast-1.images.arcpublishing.com/chosun/G2ZTVAVBKVUMMPAZQG4G65WCLQ.png"
        >
      </v-avatar>
      <p class="ml-3 white--text">
        {{ profile.username }}
      </p>
    </v-card-title>
  </v-img>
      <br>
  
      <v-list two-line class="text-left">
        <v-list-item>
          <v-list-item-icon>
            <v-icon color="indigo">
              mdi-account
            </v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>그대의 이름은.......</v-list-item-title>
            <v-list-item-title>{{ profile.username }}</v-list-item-title>
          </v-list-item-content>
  
        </v-list-item>
        <v-list-item>
          <v-list-item-icon>
            <v-icon color="indigo">
              mdi-heart
            </v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>그대와 내가 처음 만난 날.....</v-list-item-title>
            <v-list-item-title>{{ profile.date_joined.substring(0, 10) }}</v-list-item-title>
          </v-list-item-content>
  
        </v-list-item>
  
        <v-divider inset></v-divider>
        
        <v-card
          flat
          tile
        >

          <v-container
            class="grey lighten-4"
            fluid
          >
            <v-subheader class="black--text">그대가 좋아하는 영화들....❤</v-subheader>

            <v-row>
              <v-spacer></v-spacer>
              <v-col
                v-for="movie in movies"
                :key="movie.movie_id"
                cols="12"
                sm="6"
                md="4"
              >
              <v-card
              @click.stop="goDetail(movie.movie_id)">
                <v-img
                  :src="'https://image.tmdb.org/t/p/original' + movie.poster_path"
                  height="100%"
                >
                <span
                  class="text-h5 white--text pl-4 pt-4 d-inline-block"
                >
                </span>
                </v-img>
              </v-card>
              </v-col>
            </v-row>
          </v-container>
        </v-card>
      </v-list>
    </v-card>
  </div>
</template>

<script>
import axios from 'axios'

const POSTER_URL = "https://image.tmdb.org/t/p/original";

export default {
  name: "MyPageView",
  data() {
    return {
      profile: null,
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin;
    },
    movies() {
      // console.log(this.$store.state.movies)
      return this.profile.like_movies;
    },
    poster() {
      //  console.log(this.movie.pk)
      return POSTER_URL + this.movie.poster_path;
    },
  },
  created() {
    this.getAccountPage();
    this.getUserDetail();
  },
  methods: {
    getAccountPage() {
      if (this.isLogin === true) {
        console.log("로그인을 했다니 쥐엔장");
      } else {
        alert("여기서 로그인하셔야 합니다.");
        this.$router.push({ name: "LogInView" });
      }
    },
    getUserDetail() {
      axios({
        method: "get",
        url: 'http://127.0.0.1:8000/api/v1/profile',
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res)
          this.profile = res.data;
        })
        .catch((err) => {
          console.log(err);
        })
    },
    goDetail(movie_id) {
      this.$router.push({ name: "MovieDetail", params: { movie_id } });
    },
  },
};
</script>