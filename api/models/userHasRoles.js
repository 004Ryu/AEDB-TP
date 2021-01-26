const db = require("../config/db").connection;

module.exports.list = async () => {
  var conn;
  const res = [];
  try {
    conn = await db;
    const query = `SELECT UR.USER_ID, UR.ROLE_ID\
    FROM USERS_HAS_ROLES UR\
    INNER JOIN USERS U \
    ON UR.USER_ID = U.USER_ID \
    INNER JOIN ROLES R \
    ON UR.ROLE_ID = R.ROLE_ID`;
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
