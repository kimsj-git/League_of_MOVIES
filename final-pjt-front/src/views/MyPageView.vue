<template>
  <div class="mypage">
    <h1>This is an account page</h1>
    {{ profile }}
    <hr>
    <h3>그대의 이름은.......{{ profile.username }}</h3>
  </div>
</template>

<script>
import axios from 'axios'

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
  },
};
</script>