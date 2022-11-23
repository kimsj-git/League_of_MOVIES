<template>
  <div class="mypage">
    <h1>This is an account page</h1>
  </div>
</template>

<script>
export default {
  name: 'MyPageView',
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  created() {
    this.getAccountPage()
  },
  methods: {
    getAccountPage() {
      if (this.isLogin === true) {
        console.log('로그인을 했다니 쥐엔장')
      } else {
        alert('여기서 로그인하셔야 합니다.')
        this.$router.push({ name: 'LogInView' })
      }
    }
  }
}
</script>