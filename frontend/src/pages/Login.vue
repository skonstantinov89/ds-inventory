const { useQuasar } = require("quasar")


<template>

  <div class="row" style="height: 90vh">
    <div v-bind:class="{'justify-center': $q.screen.md || $q.screen.sm ||$q.screen.xs}"
         class="col-12 col-md-6 flex content-center">
      <q-card class="loginStyle" v-bind:style="$q.screen.lt.sm ? {'width': '80%'} : {'width': '50%'}">
        <q-card-section>
          <q-avatar size="103px" class="absolute-center shadow-10">
            <img src="~assets/thumbnail.png" alt="avatar">
          </q-avatar>
        </q-card-section>
        <q-card-section>
          <div class="q-pt-lg">
            <div class="col text-h6 ellipsis flex justify-center">
              <h2 class="text-h2 text-uppercase q-my-none text-weight-regular">Login</h2>
            </div>
          </div>
        </q-card-section>
        <q-card-section>
          <q-form class="q-gutter-md" @submit.prevent="submit">
            <q-input label="Username" v-model="login.username">
            </q-input>
            <q-input label="Password" type="password" v-model="login.password">
            </q-input>
            <div>
              <q-btn class="full-width" color="primary" label="Login" type="submit" rounded></q-btn>
              <div class="text-center q-mt-sm q-gutter-lg">
                <router-link class="text-white" to="/home"></router-link>
              </div>
            </div>
          </q-form>
        </q-card-section>
      </q-card>
    </div>
  </div>
</template>
<script>
import { useQuasar } from "quasar";
let $q;

export default {
  name: "LoginPage",
  data() {
    return {
      login: {
        username: "",
        password: "",
      },
    };
  },
  methods: {
    submit() {
      if (!this.login.username || !this.login.password) {
        $q.notify({
          type: "negative",
          message: "Wrong Password! Try Again",
        });
        console.log("Wrong Password!");
      } else {
        $q.notify({
          type: "positive",
          message: "Welcome!",
        });
        console.log("hello");
      }
    },
  },
  mounted() {
    $q = useQuasar();
  },
};
</script>

<style scoped>
body {
  background-color: green;
}
/* div.form {
  display: block;
  text-align: center;
  position: center;
  top: 100px;
  right: 0;
  width: 400px;
  height: 489px;
  border: 5px solid #73AD21;
}

form {
  display: inline-block;
  margin-left: auto;
  margin-right: auto;
  text-align: left;
  position: center;
  top: 100px;
  right: 0;
  width: 300px;
  height: 300x;

} */
</style>
