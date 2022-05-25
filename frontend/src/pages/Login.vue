const { useQuasar } = require("quasar")

<template>

    <div class='flex center'>
      <q-card >
        <q-card-section>
          <q-form  class="q-gutter-md" @submit.prevent="submit">
            <q-input label="Username" v-model='login.username'> </q-input>
            <q-input label="Password" type="password" v-model='login.password'> </q-input>
            <div>
              <q-btn class="full-width" color="primary" label="Login" rounded type='submit'>
              </q-btn>
            </div>
          </q-form>
        </q-card-section>
      </q-card>
    </div>


</template>

<script>
import { useQuasar } from 'quasar'
let $q

export default {
  name: "LoginPage",
  data() {
    return {
      login: {
        username: '',
        password: '',
      }
    }
  },
  methods: {
    submit() {
      if (!this.login.username || !this.login.password ) {
        $q.notify({
          type: 'negative',
          message: 'Wrong Password! Try Again'
        })
        console.log('Wrong Password!')
      }
      else{
        $q.notify({
          type: 'positive',
          message: 'Welcome!'
        })
        console.log('hello')
      }

    }
  },
  mounted(){
    $q = useQuasar()
  }
}
</script>

<style>
.center {

text-align: center;
}
</style>
