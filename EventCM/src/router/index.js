import Vue from 'vue'
import Router from 'vue-router'
import Events from '@/components/Events'
import Register from '@/components/Register'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Events',
      component: Events
    },
    {
      path: '/register?id_evento=:idEvento',
      name: 'register',
      component: Register
      // component: () =>
      // import('../components/Register.vue')
    }
  ]
})
