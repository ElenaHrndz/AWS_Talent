<template lang="html">
  <div class="register">
    <form @submit.prevent="creatUser()">
      <v-text-field
        v-model="name"
        v-validate="'required|max:20'"
        :error-messages="errors.collect('name')"
        label="Nombre"
        data-vv-name="name"
        required
      ></v-text-field>
      <v-text-field
        v-model="company"
        v-validate="'required|max:20'"
        :error-messages="errors.collect('company')"
        label="Empresa"
        data-vv-name="company"
        required
      ></v-text-field>
      <v-text-field
        v-model="puesto"
        v-validate="'required|max:10'"
        :error-messages="errors.collect('puesto')"
        label="Puesto"
        data-vv-name="puesto"
        required
      ></v-text-field>
      <v-text-field
        v-model="email"
        v-validate="'required|email'"
        :error-messages="errors.collect('email')"
        label="E-mail"
        data-vv-name="email"
        required
      ></v-text-field>
      <v-text-field
        v-model="phone"
        v-validate="'required|max:15'"
        :error-messages="errors.collect('telefono')"
        label="Telefono"
        data-vv-name="telefono"
        required
      ></v-text-field>
      <v-select
        v-model="select"
        v-validate="'required'"
        :items="items"
        :error-messages="errors.collect('select')"
        label="¿Actualmente usa AWS?"
        data-vv-name="select"
        required
      ></v-select>
      <!-- <v-checkbox
        v-model="checkbox"
        v-validate="'required'"
        :error-messages="errors.collect('checkbox')"
        value="1"
        label="Aceptar terminos"
        data-vv-name="checkbox"
        type="checkbox"
        required
      ></v-checkbox> -->

      <v-btn @click="creatUser">Registrar</v-btn>
      <v-btn @click="clear">Borrar</v-btn>
    </form>
  </div>
</template>

<script>
export default {
  $_veeValidate: {
    validator: 'new'
  },
  data: () => ({
    name: '',
    company: '',
    puesto: '',
    email: '',
    phone: '',
    select: null,
    items: [
      'Sí',
      'No'
    ],
    checkbox: null,
    dictionary: {
      attributes: {
        email: 'E-mail Address'
        // custom attributes
      },
      custom: {
        name: {
          required: () => 'El nombre no puede estar vacio',
          max: 'El nombre no debe tener más de 20 caracteres'
          // custom messages
        },
        select: {
          required: 'Select field is required'
        }
      }
    }
  }),

  mounted () {
    this.$validator.localize('en', this.dictionary)
  },

  methods: {
    submit () {
      this.$validator.validateAll()
    },
    creatUser: function () {
      var url = 'https://0nwyn7vvaa.execute-api.us-east-1.amazonaws.com/dev/create-users'
      var user = {
        'name': this.name,
        'company': this.company,
        'puesto': this.puesto,
        'email': this.email,
        'phone': this.phone,
        'select': this.select,
        'id_evento': this.id_evento.idEvento
      }

      fetch(url, {
        method: 'POST',
        body: JSON.stringify(user), // data can be `string` or {object}!
        headers: {
          'Content-Type': 'application/json'
        }
      }).then(res => res.json())
        .catch(error => console.error('Error:', error))
        .then(response => {
          console.log('Success:', response)
          this.clear()
        })
    },
    clear () {
      this.name = ''
      this.company = ''
      this.puesto = ''
      this.email = ''
      this.phone = ''
      this.select = null
      // this.checkbox = null
      this.$validator.reset()
    }
  },
  created () {
    this.id_evento = this.$route.params
  }
}
</script>

<style lang="css" scoped>
.register{
  margin: 10% 25%;
}
</style>
