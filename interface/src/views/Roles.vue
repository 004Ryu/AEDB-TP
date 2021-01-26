<template>
  <v-data-table
    :headers="headers"
    :items="roles"
    :items-per-page="20"
    class="elevation-1"
  ></v-data-table>
</template>

<script>
import axios from "axios";

export default {
  methods: {
    getRoles() {
      axios
        .get("http://localhost:4444/roles", {
          "Content-Type": "application/json",
        })
        .then((res) => {
          console.log(res.data);
          this.roles = res.data;
        })
        .catch((erro) => console.log(erro));
    },
  },
  created() {
    this.getRoles();
  },
  data() {
    return {
      headers: [
        { text: "ROLE_NAME", value: "ROLE_NAME", align: "start" },
        {
          text: "AUTHENTICATION_TYPE",
          value: "AUTHENTICATION_TYPE",
          align: "start",
        },
        { text: "COMMON", value: "COMMON", align: "start" },
        { text: "TIMESTAMP", value: "TIMESTAMP", align: "start" },
      ],
      roles: [],
    };
  },
};
</script>
