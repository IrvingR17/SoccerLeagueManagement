import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import LogIn from '@/components/LogIn'
import Index from '@/components/Index'
import RegisterLeague from '@/components/RegisterLeague'

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
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
  ],
  mode: 'history'
})
