<template>
  <v-data-table
    :headers="headers"
    :items="users"
    :items-per-page="20"
    class="elevation-1"
  ></v-data-table>
</template>

<script>
import axios from "axios";

export default {
  methods: {
    getUsers() {
      axios
        .get("http://localhost:4444/users", {
          "Content-Type": "application/json",
        })
        .then((res) => {
          console.log(res.data);
          this.users = res.data;
        })
        .catch((erro) => console.log(erro));
    },
  },
  created() {
    this.getUsers();
  },
  data() {
    return {
      headers: [
        { text: "USER_ID", value: "USER_ID", align: "start" },
        {
          text: "USERNAME",
          value: "USERNAME",
          align: "start",
        },
        { text: "ACCOUNT_STATUS", value: "ACCOUNT_STATUS", align: "start" },
        {
          text: "EXPIRY_DATE",
          value: "EXPIRY_DATE",
          align: "start",
        },
        {
          text: "DEFAULT_TABLESPACE",
          value: "DEFAULT_TABLESPACE",
          align: "start",
        },
        { text: "CREATED", value: "CREATED", align: "start" },
        { text: "COMMON", value: "COMMON", align: "start" },
        { text: "LAST_LOGIN", value: "LAST_LOGIN", align: "start" },
        { text: "PROFILE_ID", value: "PROFILE_ID", align: "start" },
        { text: "ROLE_NAME", value: "ROLE_NAME", align: "start" },
        { text: "TIMESTAMP", value: "TIMESTAMP", align: "start" },
      ],
      users: [],
    };
  },
};
</script>
