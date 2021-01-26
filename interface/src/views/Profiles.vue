<template>
  <v-simple-table dark>
    <template v-slot:default>
      <thead>
        <tr>
          <th class="text-left">
            PROFILE_ID
          </th>
          <th class="text-left">
            PROFILE_NAME
          </th>
          <th class="text-left">
            RESOURCE_NAME
          </th>
          <th class="text-left">
            RESOURCE_TYPE
          </th>
          <th class="text-left">
            LIMIT
          </th>
          <th class="text-left">
            TIMESTAMP
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in profiles" :key="item.PROFILE_ID">
          <td>{{ item.PROFILE_ID }}</td>
          <td>{{ item.PROFILE_NAME }}</td>
          <td>{{ item.RESOURCE_NAME }}</td>
          <td>{{ item.RESOURCE_TYPE }}</td>
          <td>{{ item.LIMIT }}</td>
          <td>{{ item.TIMESTAMP }}</td>
        </tr>
      </tbody>
    </template>
  </v-simple-table>
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
      profiles: [],
    };
  },
};
</script>
