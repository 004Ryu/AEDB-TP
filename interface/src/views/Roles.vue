<template>
  <v-simple-table dark>
    <template v-slot:default>
      <thead>
        <tr>
          <th class="text-left">
            ROLE_ID
          </th>
          <th class="text-left">
            ROLE_NAME
          </th>
          <th class="text-left">
            AUTHENTICATION_TYPE
          </th>
          <th class="text-left">
            COMMON
          </th>
          <th class="text-left">
            TIMESTAMP
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in roles" :key="item.ROLE_ID">
          <td>{{ item.ROLE_ID }}</td>
          <td>{{ item.ROLE_NAME }}</td>
          <td>{{ item.AUTHENTICATION_TYPE }}</td>
          <td>{{ item.COMMON }}</td>
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
      roles: [],
    };
  },
};
</script>
