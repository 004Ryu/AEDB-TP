const db = require("../config/db").connection;

module.exports.list = () => {
  const query = `SELECT USER_ID, ROLE_ID\
  FROM USERS_HAS_ROLES UR\
  INNER JOIN USERS U \
  ON UR.USER_ID = U.USER_ID \
  INNER JOIN ROLES R \
  ON UR.ROLE_ID = R.ROLE_ID`;
  return db.execute(query);
};
