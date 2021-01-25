<template>
  <v-app>
    <div class="nav">
      <router-link to="/" class="link">Instance</router-link>
      <router-link to="/cpu" class="link">CPU</router-link>
      <router-link to="/datafiles" class="link">DataFiles</router-link>
      <router-link to="/memory" class="link">Memory</router-link>
      <router-link to="/profiles" class="link">Profiles</router-link>
      <router-link to="/roles" class="link">Roles</router-link>
      <router-link to="/sessions" class="link">Sessions</router-link>
      <router-link to="/tablespaces" class="link">TableSpaces</router-link>
      <router-link to="/users" class="link">Users</router-link>
    </div>
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",

  components: {},

  methods: {},

  data: () => ({}),
};
</script>

<style scoped>
.nav {
  display: grid;
  grid-template-columns: 11% 11% 11% 11% 11% 11% 11% 11% 11%;
  justify-items: center;
}

.link {
  text-decoration: none;
  margin: 10px 0px;
}
</style>
