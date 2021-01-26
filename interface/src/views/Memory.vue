<template>
  <v-data-table
    :headers="headers"
    :items="memory"
    :items-per-page="20"
    class="elevation-1"
  ></v-data-table>
</template>

<script>
import axios from "axios";

export default {
  methods: {
    getMemory() {
      axios
        .get("http://localhost:4444/memory", {
          "Content-Type": "application/json",
        })
        .then((res) => {
          console.log(res.data);
          this.memory = res.data;
        })
        .catch((erro) => console.log(erro));
    },
  },
  created() {
    this.getMemory();
  },
  data() {
    return {
      headers: [
        { text: "FIXED_SIZE", value: "FIXED_SIZE", align: "start" },
        { text: "VARIABLE_SIZE", value: "VARIABLE_SIZE", align: "start" },
        { text: "DATABASE_BUFFERS", value: "DATABASE_BUFFERS", align: "start" },
        { text: "REDO_BUFFERS", value: "REDO_BUFFERS", align: "start" },
        { text: "TIMESTAMP", value: "TIMESTAMP", align: "start" },
      ],
      memory: [],
    };
  },
};
</script>
