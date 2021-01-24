const db = require("../config/db").connection;

module.exports.list = () => {
  const query = `SELECT MEMORY_ID, FIXED_SIZE, VARIABLE_SIZE, DATABASE_BUFFERS, REDO_BUFFERS, TIMESTAMP, DB_ID \
  FROM MEMORY \
  INNER JOIN DATABASE_INSTANCE DBI \
  ON MEMORY.DB_ID = DBI_DB_ID \
  WHERE TIMESTAMP = SYSDATE`;
  return db.execute(query);
};
