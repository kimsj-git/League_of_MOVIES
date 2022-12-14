import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000/'
const TMDB_API_URL = 'https://api.themoviedb.org/3/'
const TMDB_API_KEY = process.env.VUE_APP_TMDB_API_KEY

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    movies: [],
    latestMovies: [],
    genres: [],
    matches: [],
    username: '',
    token: null,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    LOAD_MOVIE(state, movies) {
      state.movies = movies
    },
    LOAD_GENRE(state, genres) {
      state.genres = genres
    },
    GET_LATEST_MOVIES(state, latestMovies) {
      state.latestMovies = latestMovies
    },
    // SIGN_UP(state, token) {
    //   state.token = token
    // },
    GET_MATCHES(state, matches) {
      state.matches = matches
    },
    SAVE_TOKEN(state, token, username) {
      state.token = token
      state.username = username
      router.push({name: 'LeagueView'})
    },
    REMOVE_TOKEN(state) {
      localStorage.clear()
      state.token = null
      // location.reload();
    }
  },
  actions: {
    getMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}api/v1/movies/`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        }
      })
        .then((res) => {
          // console.log(res.data)
          context.commit('LOAD_MOVIE', res.data)
        })
        .catch((err) => {
          console.log(err)
        })

    },
    getGenres(context) {
      axios({
        method: 'get',
        url: `${API_URL}api/v1/genre/`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        }
      })
        .then((res) => {
          console.log(res.data)
          context.commit('LOAD_GENRE', res.data)
        })
        .catch((err) => {
          console.log(err)
        })

    },
    getLatestMovies(context) {
      axios({
        method: 'get',
        url: `${TMDB_API_URL}movie/top_rated?api_key=${TMDB_API_KEY}&language=ko-KR&page=1`
      })
        .then((res) => {
          console.log(res.data, context)
          context.commit('GET_LATEST_MOVIES', res.data.results)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getMatches(context) {
      axios({
        method: 'get',
        url: `${API_URL}api/v1/league/`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        }
      })
        .then((res) => {
          context.commit('GET_MATCHES', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: 'post',
        url: `${API_URL}accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
        .then((res) => {
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    logIn(context, payload) {
      const username = payload.username
      const password = payload.password

      axios({
        method: 'post',
        url: `${API_URL}accounts/login/`,
        data: {
          username, password
        }
      })
        .then((res) => {
          context.commit('SAVE_TOKEN', res.data.key, res.data.username)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    logOut(context) {
      axios({
        method: 'post',
        url: `${API_URL}accounts/logout/`
      })
        .then((res) => {
          console.log(res)
          context.commit('REMOVE_TOKEN')
        })
        .catch((err) => {
          console.log(err)
        })
    },
    saveParamsToSessionStorage(context, match_pk) {
      const jsonParams = JSON.stringify(match_pk)
      sessionStorage.setItem('params', jsonParams)
    }
  
  },
  modules: {
  }
})