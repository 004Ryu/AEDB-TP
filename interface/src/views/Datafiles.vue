<template>
  <v-data-table
    :headers="headers"
    :items="datafiles"
    :items-per-page="20"
    class="elevation-1"
  ></v-data-table>
</template>

<script>
import axios from "axios";

export default {
  methods: {
    getDatafiles() {
      axios
        .get("http://localhost:4444/datafiles", {
          "Content-Type": "application/json",
        })
        .then((res) => {
          console.log(res.data);
          this.datafiles = res.data;
        })
        .catch((erro) => console.log(erro));
    },
  },
  created() {
    this.getDatafiles();
  },
  data() {
    return {
      headers: [
        { text: "DATAFILE_NAME", value: "DATAFILE_NAME", align: "start" },
        { text: "DIRECTORY", value: "DIRECTORY", align: "start" },
        { text: "TOTAL_SPACE", value: "TOTAL_SPACE", align: "start" },
        { text: "AUTOEXTENSIBLE", value: "AUTOEXTENSIBLE", align: "start" },
        {
          text: "FREE_SPACE",
          value: "FREE_SPACE",
          align: "start",
        },
        { text: "STATUS", value: "STATUS", align: "start" },
        { text: "TABLESPACE_ID", value: "TABLESPACE_ID", align: "start" },
        { text: "TIMESTAMP", value: "TIMESTAMP", align: "start" },
      ],
      datafiles: [],
    };
  },
};
</script>
