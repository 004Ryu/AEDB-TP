<template>
  <v-app>
    <div class="nav">
      <router-link to="/">Instance</router-link>
      <router-link to="/cpu">CPU</router-link>
      <router-link to="/datafiles">DataFiles</router-link>
      <router-link to="/memory">Memory</router-link>
      <router-link to="/profiles">Profiles</router-link>
      <router-link to="/roles">Roles</router-link>
      <router-link to="/sessions">Sessions</router-link>
      <router-link to="/tablespaces">TableSpaces</router-link>
      <router-link to="/users">Users</router-link>
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

  data: () => ({
    //
  }),
};
</script>
