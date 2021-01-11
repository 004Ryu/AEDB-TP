const db = require("../config/db").connection;

module.exports.list = () => {
  const query = `SELECT ROLE_ID, ROLE_NAME, AUTHENTICATION_TYPE, COMMON, TIMESTAMP \
  FROM ROLES \
  WHERE TIMESTAMP = SYSDATE`;
  return db.execute(query);
};
