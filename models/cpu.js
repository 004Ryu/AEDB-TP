const db = require("../config/db").connection;

module.exports.list = () => {
  const query = `SELECT CPU_ID, DB_ID, SQL_ID, EXECUTIONS_DELTA. BUFFER_GETS_DELTA, DISK_READS_DELTA, IOWAIT_DELTA, APWAIT_DELTA, \
  CPU_TIME_DELTA, ELAPSED_TIME_DELTA, TIMESTAMP \
  FROM CPU \
  INNER JOIN DATABASE_INSTANCE DBI ON CPU.DB_ID = CPU.DB_ID \
  WHERE TIMESTAMP = SYSDATE`;
  return db.execute(query);
};
