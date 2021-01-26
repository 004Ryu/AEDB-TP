<template>
  <v-simple-table dark>
    <template v-slot:default>
      <thead>
        <tr>
          <th class="text-left">
            DATAFILE_ID
          </th>
          <th class="text-left">
            DATAFILE_NAME
          </th>
          <th class="text-left">
            DIRECTORY
          </th>
          <th class="text-left">
            TOTAL_SPACE
          </th>
          <th class="text-left">
            AUTOEXTENSIBLE
          </th>
          <th class="text-left">
            FREE_SPACE
          </th>
          <th class="text-left">
            STATUS
          </th>
          <th class="text-left">
            TABLESPACE_ID
          </th>
          <th class="text-left">
            TIMESTAMP
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in datafiles" :key="item.DATAFILE_ID">
          <td>{{ item.DATAFILE_ID }}</td>
          <td>{{ item.DATAFILE_NAME }}</td>
          <td>{{ item.DIRECTORY }}</td>
          <td>{{ item.TOTAL_SPACE }}</td>
          <td>{{ item.AUTOEXTENSIBLE }}</td>
          <td>{{ item.FREE_SPACE }}</td>
          <td>{{ item.STATUS }}</td>
          <td>{{ item.TABLESPACE_ID }}</td>
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
    getDatafiles() {
      axios
        .get("http://localhost:4444/datafiles", {
          "Content-Type": "application/json",
        })
        .then((res) => {
          console.log(res.data);
          this.datafiles = res.data;
        })
        .catch((erro) => console.log(erro));
    },
  },
  created() {
    this.getDatafiles();
  },
  data() {
    return {
      datafiles: [],
    };
  },
};
</script>
