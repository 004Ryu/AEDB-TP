const db = require("../config/db").connection;

module.exports.list = () => {
  var conn;
  const res = [];
  try {
    conn = await db;
    const query = `SELECT ROLE_ID, ROLE_NAME, AUTHENTICATION_TYPE, COMMON, TIMESTAMP \
    FROM ROLES \
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
