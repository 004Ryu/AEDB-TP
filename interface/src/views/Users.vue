<template>
  <v-simple-table dark>
    <template v-slot:default>
      <thead>
        <tr>
          <th class="text-left">
            USER_ID
          </th>
          <th class="text-left">
            USERNAME
          </th>
          <th class="text-left">
            ACCOUNT_STATUS
          </th>
          <th class="text-left">
            EXPIRY_DATE
          </th>
          <th class="text-left">
            DEFAULT_TABLESPACE
          </th>
          <th class="text-left">
            TEMPORARY_TABLESPACE
          </th>
          <th class="text-left">
            CREATED
          </th>
          <th class="text-left">
            COMMON
          </th>
          <th class="text-left">
            LAST_LOGIN
          </th>
          <th class="text-left">
            TIMESTAMP
          </th>
          <th class="text-left">
            PROFILE_ID
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in users" :key="item.USER_ID">
          <td>{{ item.USER_ID }}</td>
          <td>{{ item.USERNAME }}</td>
          <td>{{ item.ACCOUNT_STATUS }}</td>
          <td>{{ item.EXPIRY_DATE }}</td>
          <td>{{ item.DEFAULT_TABLESPACE }}</td>
          <td>{{ item.TEMPORARY_TABLESPACE }}</td>
          <td>{{ item.CREATED }}</td>
          <td>{{ item.COMMON }}</td>
          <td>{{ item.LAST_LOGIN }}</td>
          <td>{{ item.TIMESTAMP }}</td>
          <td>{{ item.PROFILE_ID }}</td>
        </tr>
      </tbody>
    </template>
  </v-simple-table>
</template>

<script>
import axios from "axios";

export default {
  methods: {
    getUsers() {
      axios
        .get("localhost:4444/users")
        .then((res) => (this.users = res.data))
        .catch((erro) => console.log(erro));
    },
  },
  data() {
    return {
      users: [],
    };
  },
};
</script>
