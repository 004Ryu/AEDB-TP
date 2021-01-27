const db = require("../config/db").connection;

module.exports.list = async () => {
  var conn;
  const res = [];
  try {
    conn = await db;
    const query = `SELECT U.USER_ID, U.USERNAME, U.ACCOUNT_STATUS, U.EXPIRY_DATE, U.DEFAULT_TABLESPACE, U.CREATED, \
    U.COMMON, U.LAST_LOGIN, U.TIMESTAMP, U.PROFILE_ID, R.ROLE_NAME \
    FROM TRABALHOPDB.USERS U \
    INNER JOIN TRABALHOPDB.USERS_HAS_ROLES H ON U.USER_ID = H.USER_ID \
    INNER JOIN TRABALHOPDB.ROLES R ON H.ROLE_ID = R.ROLE_ID \
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
