const db = require("../config/db").connection;

module.exports.list = () => {
  var conn;
  const res = [];
  try {
    conn = await db;
    const query = `SELECT USER_ID, USERNAME, ACCOUNT_STATUS, EXPIRY_DATE, DEFAULT_TABLESPACE, TEMPORARY_TABLESPACE, CREATED, \
    COMMON, LAST_LOGIN, TIMESTAMP, PROFILE_ID \
    FROM USERS \
    INNER JOIN PROFILES P \
    ON USERS.PROFILE_ID = P.PROFILE_ID \
    WHERE TIMESTAMP = SYSDATE AND LAST_LOGIN = SYSDATE`;
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
