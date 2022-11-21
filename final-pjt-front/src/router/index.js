import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import NotFound404 from '@/views/NotFound404'
import SignUpView from '@/views/SignUpView'
import LogInView from '@/views/LogInView'
import LogOutView from '@/views/LogOutView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView
  },
  {
    path: '/league',
    name: 'LeagueView',
    component: () => import(/* webpackChunkName: "about" */ '../views/LeagueView.vue')
  },
  // 욕망기능...
  // {
  //   path: '/worldcup',
  //   name: 'worldcup',
  //   component: () => import('../views/WorldcupView.vue')
  // },
  {
    path: '/mypage',
    name: 'mypage',
    component: () => import('../views/MyPageView.vue')
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
    path: 'movie/:id',
    name: 'MovieDetail',
    component: () => import('../components/MovieDetail.vue')
  },
  {
    path: 'league/:id',
    name: 'LeagueDetail',
    component: () => import('../components/LeagueDetail.vue')
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },
  {
    path: '/login',
    name: 'LogInView',
    component: LogInView
  },
  {
    path: '/logout',
    name: 'LogOutView',
    component: LogOutView
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
