<template>
  <v-simple-table dark>
    <template v-slot:default>
      <thead>
        <tr>
          <th class="text-left">
            SESSION_ID
          </th>
          <th class="text-left">
            SAMPLE_TIME
          </th>
          <th class="text-left">
            SQL_ID
          </th>
          <th class="text-left">
            SQL_OP_NAME
          </th>
          <th class="text-left">
            SQL_PLAN_OPERATION
          </th>
          <th class="text-left">
            WAIT_CLASS
          </th>
          <th class="text-left">
            WAIT_TIME
          </th>
          <th class="text-left">
            SESSION_TYPE
          </th>
          <th class="text-left">
            SESSION_STATE
          </th>
          <th class="text-left">
            TIME_WAITED
          </th>
          <th class="text-left">
            USER_ID
          </th>
          <th class="text-left">
            TIMESTAMP
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in sessions" :key="item.SESSION_ID">
          <td>{{ item.SESSION_ID }}</td>
          <td>{{ item.SAMPLE_TIME }}</td>
          <td>{{ item.SQL_ID }}</td>
          <td>{{ item.SQL_OP_NAME }}</td>
          <td>{{ item.SQL_PLAN_OPERATION }}</td>
          <td>{{ item.WAIT_CLASS }}</td>
          <td>{{ item.WAIT_TIME }}</td>
          <td>{{ item.SESSION_TYPE }}</td>
          <td>{{ item.SESSION_STATE }}</td>
          <td>{{ item.TIME_WAITED }}</td>
          <td>{{ item.USER_ID }}</td>
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
      sessions: [],
    };
  },
};
</script>
