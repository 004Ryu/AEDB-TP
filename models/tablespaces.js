const db = require("../config/db").connection;

module.exports.list = () => {
  const query = `SELECT TABLESPACE_ID, TABLESPACE_NAME, STATUS, TYPE, SEGMENT_SPACE_MANAGEMENT, TIMESTAMP, DB_ID \
  FROM TABLESPACES \
  INNER JOIN DATABASE_INSTANCE DBI ON TABLESPACES.DB_ID = DBI.DB_ID \
  WHERE TIMESTAMP = SYSDATE`;
  return db.execute(query);
};
