import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "DatabaseInstance",
    component: () => import("../views/Instance.vue"),
  },
  {
    path: "/cpu",
    name: "CPU",
    component: () => import("../views/Cpu.vue"),
  },
  {
    path: "/datafiles",
    name: "DataFiles",
    component: () => import("../views/Datafiles.vue"),
  },
  {
    path: "/memory",
    name: "Memory",
    component: () => import("../views/Memory.vue"),
  },
  {
    path: "/profiles",
    name: "Profiles",
    component: () => import("../views/Profiles.vue"),
  },
  {
    path: "/roles",
    name: "Roles",
    component: () => import("../views/Roles.vue"),
  },
  {
    path: "/sessions",
    name: "Sessions",
    component: () => import("../views/Sessions.vue"),
  },
  {
    path: "/tablespaces",
    name: "TableSpaces",
    component: () => import("../views/Tablespaces.vue"),
  },
  {
    path: "/users",
    name: "Users",
    component: () => import("../views/Users.vue"),
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
