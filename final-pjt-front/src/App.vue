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
          <v-btn depressed>League</v-btn>
        </router-link>

        <router-link to="/match-ranking">
          <v-btn depressed>Ranking</v-btn>
        </router-link>
        
        <router-link to="/mypage">
          <v-btn depressed>My Page</v-btn>
        </router-link>
        
        <!-- <router-link to="/signup">
          <v-btn depressed>signup</v-btn>
        </router-link> -->
        
        <router-link to="/login" v-if="!isLogin">
          <v-btn depressed>Login</v-btn>
        </router-link>
        
        <router-link
          class="logoutButton"
          @click.native="logout"
          to="/logout"
          v-if="isLogin"
        >
          <v-btn depressed>logout</v-btn>
        </router-link>
      </nav>

      <v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" temporary right fixed>
      <v-list nav dense>
        <v-list-item-group
          v-model="group"
          active-class="white--text text--accent-4"
        >
          <v-list-item>
            <v-list-item-icon>
              <v-icon>mdi-home</v-icon>
            </v-list-item-icon>
            <v-list-item-title>
              <router-link to="/" class="white--text" style="text-decoration: none">
              League
              </router-link>
            </v-list-item-title>
          </v-list-item>

          <v-list-item class="hidden-md-and-up">
            <v-list-item-icon>
              <v-icon>mdi-heart</v-icon>
            </v-list-item-icon>
            <v-list-item-title>
              <router-link to="/match-ranking" class="white--text" style="text-decoration: none">
              Ranking
              </router-link>
            </v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-icon>
              <v-icon>mdi-account</v-icon>
            </v-list-item-icon>
            <v-list-item-title>
              <router-link to="/mypage" class="white--text" style="text-decoration: none">
              MyPage
              </router-link>
            </v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-icon>
              <v-icon>mdi-heart</v-icon>
            </v-list-item-icon>
            <v-list-item-title>
              <router-link to="/ranking" class="white--text" style="text-decoration: none">
              '͡ ° ͜ʖ ͡  그대가 좋아할만한...영화
              </router-link>
            </v-list-item-title>
          </v-list-item>

          <v-list-item v-if="isLogin" class="hidden-md-and-up">
            <v-list-item-icon>
              <v-icon>mdi-account</v-icon>
            </v-list-item-icon>
            <v-list-item-title>
              <router-link 
              @click.native="logout"
              to="/logout"
              v-if="isLogin"
              class="white--text" 
              style="text-decoration: none">
              LogOut
              </router-link>
            </v-list-item-title>
          </v-list-item>

          <v-list-item v-if="!isLogin" class="hidden-md-and-up">
            <v-list-item-icon>
              <v-icon>mdi-account</v-icon>
            </v-list-item-icon>
            <v-list-item-title>
              <router-link to="/login" class="white--text" style="text-decoration: none">
              LogIn
              </router-link>
            </v-list-item-title>
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
