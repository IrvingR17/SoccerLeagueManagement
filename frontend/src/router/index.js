import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import ListPlayers from '@/components/users/ListPlayers'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/players',
      name: 'ListPlayers',
      component: ListPlayers
    }
  ],
  mode: 'history'
})
