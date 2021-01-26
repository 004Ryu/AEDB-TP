const db = require("../config/db").connection;

module.exports.list = async () => {
  var conn;
  const res = [];
  try {
    conn = await db;
    const query = `SELECT d.DATAFILE_ID, d.DATAFILE_NAME, d.DIRECTORY, d.TOTAL_SPACE, d.AUTOEXTENSIBLE, d.FREE_SPACE, d.STATUS, d.TIMESTAMP, d.TABLESPACE_ID \
    FROM TRABALHOPDB.DATAFILES d \
    INNER JOIN TRABALHOPDB.TABLESPACES t \
    ON d.TABLESPACE_ID = t.TABLESPACE_ID \
    ORDER BY TIMESTAMP DESC \
    FETCH FIRST 300 ROWS ONLY`;
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
