<template>
  <div id="app">
    <nav class="navbar" style="background-color: #e3f2fd;">
      <router-link to="/">Home</router-link>
      <router-link to="/league">League</router-link>
      <router-link to="/mypage">MyPage</router-link>
      <router-link to="/signup">SignUp</router-link>
      <router-link to="/login">LogIn</router-link>
      <router-link class="logoutButton" @click.prevent="logout" to="/logout">Logout</router-link>
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'AppView',
  methods: {
    logout() {
      this.$store.dispatch('logOut')
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
