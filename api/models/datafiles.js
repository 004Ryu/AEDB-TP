const db = require("../config/db").connection;

module.exports.list = async () => {
  var conn;
  const res = [];
  try {
    conn = await db;
    const query = `SELECT DATAFILE_ID, DATAFILE_NAME, DIRECTORY, TOTAL_SPACE, AUTOEXTENSIBLE, FREE_SPACE, STATUS, TIMESTAMP, TABLESPACE_ID, \
    DB_ID FROM DATAFILES \
    INNER JOIN TABLESPACES T \
    ON DATAFILES.TABLESPACE_ID = T.TABLESPACE_ID \
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
