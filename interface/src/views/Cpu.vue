<template>
  <v-simple-table dark>
    <template v-slot:default>
      <thead>
        <tr>
          <th class="text-left">
            CPU_ID
          </th>
          <th class="text-left">
            DB_ID
          </th>
          <th class="text-left">
            SQL_ID
          </th>
          <th class="text-left">
            EXECUTIONS_DELTA
          </th>
          <th class="text-left">
            BUFFER_GETS_DELTA
          </th>
          <th class="text-left">
            DISK_READS_DELTA
          </th>
          <th class="text-left">
            IOWAIT_DELTA
          </th>
          <th class="text-left">
            APWAIT_DELTA
          </th>
          <th class="text-left">
            CPU_TIME_DELTA
          </th>
          <th class="text-left">
            ELAPSED_TIME_DELTA
          </th>
          <th class="text-left">
            TIMESTAMP
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in cpu" :key="item.CPU_ID">
          <td>{{ item.CPU_ID }}</td>
          <td>{{ item.DB_ID }}</td>
          <td>{{ item.SQL_ID }}</td>
          <td>{{ item.EXECUTIONS_DELTA }}</td>
          <td>{{ item.BUFFER_GETS_DELTA }}</td>
          <td>{{ item.DISK_READS_DELTA }}</td>
          <td>{{ item.IOWAIT_DELTA }}</td>
          <td>{{ item.APWAIT_DELTA }}</td>
          <td>{{ item.CPU_TIME_DELTA }}</td>
          <td>{{ item.ELAPSED_TIME_DELTA }}</td>
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
    getCPU() {
      axios
        .get("localhost:4444/cpu")
        .then((res) => (this.cpu = res.data))
        .catch((erro) => console.log(erro));
    },
  },
  data() {
    return {
      cpu: [],
    };
  },
};
</script>
