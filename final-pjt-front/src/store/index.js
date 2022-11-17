import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000/'
const TMDB_API_URL = 'https://api.themoviedb.org/3/'
const TMDB_API_KEY = process.env.TMDB_API_KEY

export default new Vuex.Store({
  state: {
    movies: [],
    latestMovies: [],
  },
  getters: {
  },
  mutations: {
    LOAD_MOVIE(state, movies) {
      state.movies = movies
    },
    GET_LATEST_MOVIES(state, latestMovies) {
      state.latestMovies = latestMovies
    }
  },
  actions: {
    getMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}api/v1/tmdb/toprated`,
      })
        .then((res) => {
          // console.log(res.data)
          context.commit('LOAD_MOVIE', res.data)
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
    }
  
  },
  modules: {
  }
})