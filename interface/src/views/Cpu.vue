<template>
  <v-data-table
    :headers="headers"
    :items="cpu"
    :items-per-page="20"
    class="elevation-1"
  ></v-data-table>
</template>

<script>
import axios from "axios";

export default {
  methods: {
    getCPU() {
      axios
        .get("http://localhost:4444/cpu", {
          "Content-Type": "application/json",
        })
        .then((res) => {
          this.cpu = res.data;
        })
        .catch((erro) => console.log(erro));
    },
  },
  created() {
    this.getCPU();
  },
  data() {
    return {
      headers: [
        { text: "CPU_ID", value: "CPU_ID", align: "start" },
        { text: "DB_ID", value: "DB_ID", align: "start" },
        { text: "SQL_ID", value: "SQL_ID", align: "start" },
        { text: "EXECUTIONS_DELTA", value: "EXECUTIONS_DELTA", align: "start" },
        {
          text: "BUFFER_GETS_DELTA",
          value: "BUFFER_GETS_DELTA",
          align: "start",
        },
        { text: "DISK_READS_DELTA", value: "DISK_READS_DELTA", align: "start" },
        { text: "IOWAIT_DELTA", value: "IOWAIT_DELTA", align: "start" },
        { text: "APWAIT_DELTA", value: "APWAIT_DELTA", align: "start" },
        { text: "CPU_TIME_DELTA", value: "CPU_TIME_DELTA", align: "start" },
        {
          text: "ELAPSED_TIME_DELTA",
          value: "ELAPSED_TIME_DELTA",
          align: "start",
        },
        { text: "TIMESTAMP", value: "TIMESTAMP", align: "start" },
      ],
      cpu: [],
    };
  },
};
</script>
