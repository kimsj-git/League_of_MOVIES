import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import NotFound404 from '@/views/NotFound404'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/league',
    name: 'league',
    component: () => import(/* webpackChunkName: "about" */ '../views/LeagueView.vue')
  },
  // 욕망기능...
  // {
  //   path: '/worldcup',
  //   name: 'worldcup',
  //   component: () => import('../views/WorldcupView.vue')
  // },
  {
    path: '/account',
    name: 'account',
    component: () => import('../views/AccountView.vue')
  },
  {
    path: '/match-ranking',
    name: 'match-ranking',
    component: () => import('../components/MatchRanking.vue')
  },
  {
    path: '/vote-ranking',
    name: 'vote-ranking',
    component: () => import('../components/VoteRanking.vue')
  },
  {
    path: '/latest',
    name: 'latest',
    component: () => import('../views/LatestMovieView.vue')
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '*',
    redirect: '/404'
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
