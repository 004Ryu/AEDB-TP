const db = require("../config/db").connection;

module.exports.list = () => {
  const query = `SELECT DATAFILE_ID, DATAFILE_NAME, DIRECTORY, TOTAL_SPACE, AUTOEXTENSIBLE, FREE_SPACE, STATUS, TIMESTAMP, TABLESPACE_ID, \
  DB_ID FROM DATAFILES \
  INNER JOIN TABLESPACES T \
  ON DATAFILES.TABLESPACE_ID = T.TABLESPACE_ID \
  WHERE TIMESTAMP = SYSDATE`;
  return db.execute(query);
};
