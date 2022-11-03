import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import LogIn from '@/components/LogIn'
import Index from '@/components/Index'
import RegisterLeague from '@/components/RegisterLeague'
import League from '@/components/League'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/login',
      name: 'LogIn',
      component: LogIn
    },
    {
      path: '/index',
      name: 'Index',
      component: Index
    },
    {
      path: '/register_league',
      name: 'RegisterLeague',
      component: RegisterLeague
    },
    {
      path: '/league/:id',
      name: 'League',
      component: League
    },
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
  ],
  mode: 'history'
})
