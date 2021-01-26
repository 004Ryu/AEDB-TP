<template>
  <v-data-table
    :headers="headers"
    :items="tablespaces"
    :items-per-page="20"
    class="elevation-1"
  ></v-data-table>
</template>

<script>
import axios from "axios";

export default {
  methods: {
    getTablespaces() {
      axios
        .get("http://localhost:4444/tablespaces", {
          "Content-Type": "application/json",
        })
        .then((res) => {
          console.log(res.data);
          this.tablespaces = res.data;
        })
        .catch((erro) => console.log(erro));
    },
  },
  created() {
    this.getTablespaces();
  },
  data() {
    return {
      headers: [
        { text: "TABLESPACE_ID", value: "TABLESPACE_ID", align: "start" },
        {
          text: "TABLESPACE_NAME",
          value: "TABLESPACE_NAME",
          align: "start",
        },
        { text: "STATUS", value: "STATUS", align: "start" },
        {
          text: "TYPE",
          value: "TYPE",
          align: "start",
        },
        {
          text: "SEGMENT_SPACE_MANAGEMENT",
          value: "SEGMENT_SPACE_MANAGEMENT",
          align: "start",
        },
        { text: "TIMESTAMP", value: "TIMESTAMP", align: "start" },
      ],
      tablespaces: [],
    };
  },
};
</script>
