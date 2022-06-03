const routes = [
  {
    path: "/home",
    component: () => import("layouts/MainLayout.vue"),
    children: [{ path: "/test/dashboard", component: () => import("pages/HomePage.vue") }],
  },
  // {
  //   path: "/home",
  //   component: () => import("pages/HomePage.vue"),
  // },
  // {
  //   path: "/",
  //   component: () => import("pages/Login.vue"),
  // },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: "/:catchAll(.*)*",
    component: () => import("pages/ErrorNotFound.vue"),
  },
];

export default routes;
