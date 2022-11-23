<template>
  <v-app class="mx-auto overflow-hidden" height="400">
    <v-app-bar app color="dark" dark>
      <v-img
        alt="img"
        class="shrink mr-2"
        contain
        src="./assets/lol.png"
        transition="scale-transition"
        width="40"
      />
      <router-link to="/" class="white--text" style="text-decoration: none">
        <v-app-bar-title>League of Movies </v-app-bar-title>
      </router-link>

      <v-spacer></v-spacer>

      <nav class="navbar shrink mt-1 hidden-sm-and-down">
        <router-link to="/">
          <v-btn depressed>Home</v-btn>
        </router-link>

        <router-link to="/league">
          <v-btn depressed>League</v-btn>
        </router-link>
        
        <router-link to="/mypage">
          <v-btn depressed>My Page</v-btn>
        </router-link>
        
        <router-link to="/signup">
          <v-btn depressed>signup</v-btn>
        </router-link>
        
        <router-link to="/login">
          <v-btn depressed>Login</v-btn>
        </router-link>
        
        <router-link
          class="logoutButton"
          @click.native="logout"
          to="/logout"
        >
          <v-btn depressed>logout</v-btn>
        </router-link>
      </nav>

      <v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" absolute temporary right>
      <v-list nav dense>
        <v-list-item-group
          v-model="group"
          active-class="deep-purple--text text--accent-4"
        >
          <v-list-item>
            <v-list-item-icon>
              <v-icon>mdi-home</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Home</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-icon>
              <v-icon>mdi-account</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Account</v-list-item-title>
          </v-list-item>
          <v-list-item>
            <v-list-item-icon>
              <v-icon>mdi-heart</v-icon>
            </v-list-item-icon>
            <v-list-item-title>내가 좋아하는 영화</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>

    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "AppView",
  data() {
    return {
      drawer: false,
      group: null,
    };
  },
  methods: {
    logout() {
      this.$store.dispatch("logOut");
    },
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin;
    },
  },
};
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
  /* color: #2c3e50; */
  text-decoration: none;
  color: white;
}

nav a.router-link-exact-active {
  color: #42b983;
  text-decoration: none;
}
</style>
