const db = require("../config/db").connection;

module.exports.list = async () => {
  var conn;
  const res = [];
  try {
    conn = await db;
    const query = `SELECT s.SESSION_ID, s.SAMPLE_TIME, s.SQL_ID, s.SQL_OP_NAME, s.SQL_PLAN_OPERATION, s.WAIT_CLASS, s.WAIT_TIME, s.\
    SESSION_TYPE, s.SESSION_STATE, s.TIME_WAITED, s.TIMESTAMP, s.USER_ID \
    FROM TRABALHOPDB.SESSIONS s \
    INNER JOIN TRABALHOPDB.USERS u \
    ON u.USER_ID = s.USER_ID \
    ORDER BY TIMESTAMP DESC`;
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
