const db = require("../config/db").connection;

module.exports.list = () => {
  var conn;
  const res = [];
  try {
    conn = await db;
    const query = `SELECT TABLESPACE_ID, TABLESPACE_NAME, STATUS, TYPE, SEGMENT_SPACE_MANAGEMENT, TIMESTAMP, DB_ID \
    FROM TABLESPACES \
    INNER JOIN DATABASE_INSTANCE DBI ON TABLESPACES.DB_ID = DBI.DB_ID \
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
