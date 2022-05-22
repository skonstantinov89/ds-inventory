/* eslint-disable */
<template>

    <div class='flex center'>
      <q-card align="center">
        <q-card-section>
          <img
            alt="Direct Logo"
            src="~assets/ds_logo.png"
            style="width: 400px; height: 400px"
          />

          <q-form class="q-gutter-md">
            <q-input label="Username"> </q-input>
            <q-input label="Password" type="password"> </q-input>
            <div>
              <q-btn class="full-width" color="primary" label="Login" rounded>
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
};
</script>

<style>
.center {

text-align: center;
}
</style>
