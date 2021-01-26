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
        .get("http://localhost:4444/tablespaces", {
          "Content-Type": "application/json",
        })
        .then((res) => {
          console.log(res.data);
          this.tablespaces = res.data;
        })
        .catch((erro) => console.log(erro));
    },
  },
  created() {
    this.getTablespaces();
  },
  data() {
    return {
      tablespaces: [],
    };
  },
};
</script>
