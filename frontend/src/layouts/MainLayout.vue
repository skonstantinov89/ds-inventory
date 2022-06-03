<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />

        <q-toolbar-title> DS Inventory </q-toolbar-title>
        <div>
          <q-btn
            icon= "logout"
            round
            flat

          />
        </div>

      </q-toolbar>
    </q-header>

    <q-drawer v-model="leftDrawerOpen" show-if-above bordered>
      <q-list>
        <q-item-label header> Dashboard </q-item-label>

        <EssentialLink
          v-for="link in essentialLinks"
          :key="link.title"
          v-bind="link"
        />
      </q-list>
    </q-drawer>

    <q-page-container>
      <q-fab
        color="orange"
        icon ="add"
        padding = "sm"
        direction = "down"
      >
        <q-fab-action
          icon='edit'
          color = "purple"
        />

        <q-fab-action
          icon="add"
          color='green'
        />

        <q-fab-action
          icon="check"
          color="blue"

        />

      </q-fab>

      <q-btn
      label = "Log File"
      icon = "print"
      color = "green"
      padding = "sm"
      />

      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent, ref } from "vue";
import EssentialLink from "components/EssentialLink.vue";

const linksList = [
  {
    title: "Dashboard",
    caption: "",
    icon: "dashboard",
    link: "http://localhost:8081/#/test",
  },
  {
    title: "Inventory",
    caption: "Check Inventory, Create, Edit, Delete",
    icon: "edit",
    link: "http://localhost:8081/#/test/dashboard",
  },
];

export default defineComponent({
  name: "MainLayout",

  components: {
    EssentialLink,
  },

  setup() {
    const leftDrawerOpen = ref(false);

    return {
      essentialLinks: linksList,
      leftDrawerOpen,
      toggleLeftDrawer() {
        leftDrawerOpen.value = !leftDrawerOpen.value;
      },
    };
  },
});
</script>

