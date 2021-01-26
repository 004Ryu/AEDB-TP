const db = require("../config/db").connection;

module.exports.list = async () => {
  var conn;
  const res = [];
  try {
    conn = await db;
    const query = `SELECT CPU_ID, DB_ID, SQL_ID, EXECUTIONS_DELTA, BUFFER_GETS_DELTA, DISK_READS_DELTA, IOWAIT_DELTA, APWAIT_DELTA, \
    CPU_TIME_DELTA, ELAPSED_TIME_DELTA, TIMESTAMP \
    FROM CPU \
    INNER JOIN DATABASE_INSTANCE DBI ON CPU.DB_ID = CPU.DB_ID \
    WHERE TIMESTAMP = SYSDATE`;
    return conn.execute(query).then((data) => {
      data.rows.forEach((row) => {
        const aux = {};
        data.metaData.forEach((header, index) => {
          aux[header.name] = row[index];
        });
        res.push(aux);
      });
      return res;
    });
  } catch (e) {
    console.log(e);
  }
};
