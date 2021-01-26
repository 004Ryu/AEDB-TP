<template>
  <v-data-table
    :headers="headers"
    :items="profiles"
    :items-per-page="20"
    class="elevation-1"
  ></v-data-table>
</template>

<script>
import axios from "axios";

export default {
  methods: {
    getProfiles() {
      axios
        .get("http://localhost:4444/profiles", {
          "Content-Type": "application/json",
        })
        .then((res) => {
          console.log(res.data);
          this.profiles = res.data;
        })
        .catch((erro) => console.log(erro));
    },
  },
  created() {
    this.getProfiles();
  },
  data() {
    return {
      headers: [
        { text: "PROFILE_NAME", value: "PROFILE_NAME", align: "start" },
        { text: "RESOURCE_NAME", value: "RESOURCE_NAME", align: "start" },
        { text: "RESOURCE_TYPE", value: "RESOURCE_TYPE", align: "start" },
        { text: "LIMIT", value: "LIMIT", align: "start" },
        { text: "TIMESTAMP", value: "TIMESTAMP", align: "start" },
      ],
      profiles: [],
    };
  },
};
</script>
