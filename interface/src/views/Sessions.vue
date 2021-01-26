<template>
  <v-data-table
    :headers="headers"
    :items="sessions"
    :items-per-page="20"
    class="elevation-1"
  ></v-data-table>
</template>

<script>
import axios from "axios";

export default {
  methods: {
    getSessions() {
      axios
        .get("http://localhost:4444/sessions", {
          "Content-Type": "application/json",
        })
        .then((res) => {
          console.log(res.data);
          this.sessions = res.data;
        })
        .catch((erro) => console.log(erro));
    },
  },
  created() {
    this.getSessions();
  },
  data() {
    return {
      headers: [
        { text: "SAMPLE_TIME", value: "SAMPLE_TIME", align: "start" },
        {
          text: "SQL_ID",
          value: "SQL_ID",
          align: "start",
        },
        { text: "SQL_OP_NAME", value: "SQL_OP_NAME", align: "start" },
        {
          text: "SQL_PLAN_OPERATION",
          value: "SQL_PLAN_OPERATION",
          align: "start",
        },
        { text: "WAIT_CLASS", value: "WAIT_CLASS", align: "start" },
        { text: "WAIT_TIME", value: "WAIT_TIME", align: "start" },
        { text: "SESSION_TYPE", value: "SESSION_TYPE", align: "start" },
        { text: "SESSION_STATE", value: "SESSION_STATE", align: "start" },
        { text: "TIME_WAITED", value: "TIME_WAITED", align: "start" },
        { text: "USER_ID", value: "USER_ID", align: "start" },
        { text: "TIMESTAMP", value: "TIMESTAMP", align: "start" },
      ],
      sessions: [],
    };
  },
};
</script>
