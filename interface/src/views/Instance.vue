<template>
  <v-card width="65%" elevation="4" style="margin: 100px auto">
    <span class="title">Database Instance Info</span>
    <div class="instance" v-for="item in Instance" :key="item.DB_ID">
      <span class="id"><b>DB_ID:</b> {{ item.DB_ID }}</span>
      <span class="number"
        ><b>INSTANCE_NUMBER:</b> {{ item.INSTANCE_NUMBER }}</span
      >
      <span class="time"><b>STARTUP_TIME:</b> {{ item.STARTUP_TIME }}</span>
      <span class="version"><b>VERSION:</b> {{ item.VERSION }}</span>
      <span class="name"><b>DB_NAME:</b> {{ item.DB_NAME }}</span>
      <span class="instanceName"
        ><b>INSTANCE_NAME:</b> {{ item.INSTANCE_NAME }}</span
      >
      <span class="platform"
        ><b>PLATFORM_NAME:</b> {{ item.PLATFORM_NAME }}</span
      >
      <span class="unique"
        ><b>DB_UNIQUE_NAME:</b> {{ item.DB_UNIQUE_NAME }}</span
      >
      <span class="threads"
        ><b>NUMBER_THREADS:</b> {{ item.NUMBER_THREADS }}</span
      >
    </div>
  </v-card>
</template>

<script>
import axios from "axios";

export default {
  methods: {
    getInstance() {
      axios
        .get("http://localhost:4444/", { "Content-Type": "application/json" })
        .then((res) => {
          console.log(res.data);
          this.Instance = res.data;
        })
        .catch((erro) => console.log(erro));
    },
  },
  created() {
    this.getInstance();
  },
  data() {
    return {
      Instance: [],
    };
  },
};
</script>

<style scoped>
.instance {
  display: grid;
  grid-template-columns: 33% 33% 33%;
  grid-template-rows: 33% 33% 33%;
  height: 200px;
  justify-items: center;
  align-items: center;
}
.title {
  display: block;
  text-align: center;
  font-size: 100%;
}
</style>
