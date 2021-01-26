const db = require("../config/db").connection;

module.exports.list = async () => {
  var conn;
  const res = [];
  try {
    conn = await db;
    const query = `SELECT u.USER_ID, u.USERNAME, u.ACCOUNT_STATUS, u.EXPIRY_DATE, u.DEFAULT_TABLESPACE, u.TEMPORARY_TABLESPACE, u.CREATED, \
    u.COMMON, u.LAST_LOGIN, u.TIMESTAMP, u.PROFILE_ID \
    FROM TRABALHOPDB.USERS u \
    INNER JOIN TRABALHOPDB.PROFILES p \
    ON u.PROFILE_ID = p.PROFILE_ID \
    WHERE u.TIMESTAMP = SYSDATE AND u.LAST_LOGIN = SYSDATE \
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
