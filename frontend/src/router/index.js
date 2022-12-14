import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import LogIn from '@/components/LogIn'
import Index from '@/components/Index'
import Leagues from '@/components/Leagues'
import RegisterLeague from '@/components/RegisterLeague'
import League from '@/components/League'
import EditLeague from '@/components/EditLeague'
import AddTeam from '@/components/AddTeam'
import Team from '@/components/Team'
import EditTeam from '@/components/EditTeam'
import Referees from '@/components/Referees'
import AddReferee from '@/components/AddReferee'
import Managers from '@/components/Managers'
import AddManager from '@/components/AddManager'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index
    },
    {
      path: '/login',
      name: 'LogIn',
      component: LogIn
    },
    {
      path: '/leagues',
      name: 'Leagues',
      component: Leagues
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
      path: '/edit_league/:id',
      name: 'EditLeague',
      component: EditLeague
    },
    {
      path: '/add_team/:id',
      name: 'AddTeam',
      component: AddTeam
    },
    {
      path: '/team/:id',
      name: 'Team',
      component: Team
    },
    {
      path: '/edit_team/:id',
      name: 'EditTeam',
      component: EditTeam
    },
    {
      path: '/referees',
      name: 'Referees',
      component: Referees
    },
    {
      path: '/add_referee/',
      name: 'AddReferee',
      component: AddReferee
    },
    {
      path: '/managers',
      name: 'Managers',
      component: Managers
    },
    {
      path: '/add_manager/',
      name: 'AddManager',
      component: AddManager
    },
  ],
  mode: 'history'
})
