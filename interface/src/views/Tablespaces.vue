<template>
  <v-simple-table dark>
    <template v-slot:default>
      <thead>
        <tr>
          <th class="text-left">
            TABLESPACE_ID
          </th>
          <th class="text-left">
            TABLESPACE_NAME
          </th>
          <th class="text-left">
            STATUS
          </th>
          <th class="text-left">
            TYPE
          </th>
          <th class="text-left">
            SEGMENT_SPACE_MANAGEMENT
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
        <tr v-for="item in tablespaces" :key="item.TABLESPACE_ID">
          <td>{{ item.TABLESPACE_ID }}</td>
          <td>{{ item.TABLESPACE_NAME }}</td>
          <td>{{ item.STATUS }}</td>
          <td>{{ item.TYPE }}</td>
          <td>{{ item.SEGMENT_SPACE_MANAGEMENT }}</td>
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
    getTablespaces() {
      axios
        .get("localhost:4444/tablespaces")
        .then((res) => (this.tablespaces = res.data))
        .catch((erro) => console.log(erro));
    },
  },
  data() {
    return {
      tablespaces: [],
    };
  },
};
</script>
