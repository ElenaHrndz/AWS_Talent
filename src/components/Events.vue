<template>
<div id="vueApp">

  <div class="title-container">
    <h1 class="title">Events List</h1>
  </div>

  <transition-group class="events" name="events">
    <div class="item" v-bind:key="item" v-for="item in items" tag="p">
      <div class="item-link-wrapper">
        <div v-if="item.link">
          <img class="item-link" v-bind:src="item.link.S">
        </div>
        <div class="gradient-overlay"></div>
        <span class="item-title">{{item.name.S}}</span>
      </div>
      <p>Fecha: {{ item.eventDate.S }}</p>
      <p>Hora: {{ item.eventHour.S }}</p>
      <p>Prerequisitos: {{ item.prerequisites.S }}</p>
      <p>Direccion: {{ item.address.S }}</p>
      <p>Capacidad: {{ item.capacity.S }}</p>
      <div class="">
        <router-link :to="{ name:'register', params: {idEvento: item.id_evento.S }}"><v-btn flat color="orange">Registrar</v-btn></router-link>
      </div>
    </div>
  </transition-group>
</div>
</template>

<script>
export default {
  data () {
    return {
      debug: true,
      items: []
    }
  },
  methods: {
    // get list of item fon the API
    loadData: function () {
      fetch('https://0nwyn7vvaa.execute-api.us-east-1.amazonaws.com/dev/list-events')
        .then(response => response.json())
        .then(data => (this.items = data.Items))
    }
  },
  created () {
    this.loadData()
  }
}
</script>

<style scoped>

 h1{
    margin-top: 5%;
 }

.title-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.item-title {
  font-size: 16pt
}

.events {
  margin-bottom: 50px;
  margin-top: 25px;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.items-enter {
  transform: scale(0.5) translatey(-80px);
  opacity: 0;
}

.items-leave-to {
  transform: translatey(30px);
  opacity: 0;
}

.items-leave-active {
  position: absolute;
  z-index: -1;
}

.item {
  transition: all .35s ease-in-out;
  margin: 20px;
  box-shadow: 0px 2px 8px lightgrey;
  border-radius: 18px;
  width: 300px;
  height: 40%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.item-link-wrapper {
  position: relative;
}

.item-link {
  width: 100%;
  /* height: 150px; */
  border-bottom-left-radius: 5px;
  border-bottom-right-radius: 5px;
  border-top-left-radius: 3px;
  border-top-right-radius: 3px;
}
</style>
