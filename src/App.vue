<template>
  <v-app>
    <v-toolbar dark class="primary">
    <!-- <i class="fas fa-bars hidden-sm-and-up" @click.stop="sideNav = !sideNav"></i> -->
      <v-toolbar-title>
        <router-link to="/" tag="span" style="cursor: pointer">EventCM</router-link>
      </v-toolbar-title>
      <!-- <v-spacer></v-spacer>
      <v-toolbar-items class="hidden-xs-only">
        <v-btn flat v-for="item in menuItems" :key="item.title" :to="item.link">
          <v-icon left dark>{{ item.icon }}</v-icon>
          {{ item.title }}
        </v-btn>
      </v-toolbar-items> -->
    </v-toolbar>

    <!-- <v-navigation-drawer absolute temporary v-model="sideNav">
      <v-list>
        <v-list-tile v-for="item in menuItems" :key="item.title" :to="item.link">
          <v-list-tile-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>{{ item.title }}</v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer> -->

    <router-view class="main"></router-view>

  </v-app>
</template>

<script>
import Events from './components/Events'

export default {
  name: 'App',
  components: {
    Events
  },
  data () {
    return {
      sideNav: null
    }
  },
  computed: {
    menuItems () {
      let menuItems = [
        // {
        //   icon: 'fas fa-user',
        //   title: 'Usuario',
        //   link: '/register'
        // }
      ]
      return menuItems
    }
  }
}
</script>

<style media="screen">

</style>
