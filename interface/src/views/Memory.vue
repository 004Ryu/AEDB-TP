<template>
  <v-simple-table dark>
    <template v-slot:default>
      <thead>
        <tr>
          <th class="text-left">
            MEMORY_ID
          </th>
          <th class="text-left">
            FIXED_SIZE
          </th>
          <th class="text-left">
            VARIABLE_SIZE
          </th>
          <th class="text-left">
            DATABASE_BUFFERS
          </th>
          <th class="text-left">
            REDO_BUFFERS
          </th>
          <th class="text-left">
            TIMESTAMP
          </th>
          <th class="text-left">
            DB_ID
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in memory" :key="item.MEMORY_ID">
          <td>{{ item.MEMORY_ID }}</td>
          <td>{{ item.FIXED_SIZE }}</td>
          <td>{{ item.VARIABLE_SIZE }}</td>
          <td>{{ item.DATABASE_BUFFERS }}</td>
          <td>{{ item.REDO_BUFFERS }}</td>
          <td>{{ item.TIMESTAMP }}</td>
          <td>{{ item.DB_ID }}</td>
        </tr>
      </tbody>
    </template>
  </v-simple-table>
</template>

<script>
import axios from "axios";

export default {
  methods: {
    getMemory() {
      axios
        .get("localhost:4444/memory")
        .then((res) => (this.memory = res.data))
        .catch((erro) => console.log(erro));
    },
  },
  data() {
    return {
      memory: [],
    };
  },
};
</script>
