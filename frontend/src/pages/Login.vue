/* eslint-disable */
<template>

    <div class='flex center'>
      <q-card align="center">
        <q-card-section>
          <img
            alt="Direct Logo"
            src="~assets/ds_logo.png"
            style="width: 400; height: 400px"
          />

          <q-form class="q-gutter-md" @submit.prevent='submit'>
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
        log.console('error')
      }
      else{
        console.log('hello')
      }

    }
  }
};
</script>

<style>
.center {

text-align: center;
}
</style>
