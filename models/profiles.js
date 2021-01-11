const db = require("../config/db").connection;

module.exports.list = () => {
  const query = `SELECT PROFILE_ID, PROFILE_NAME, RESOURCE_NAME, RESOURCE_TYPE, LIMIT, TIMESTAMP \
  FROM PROFILES \
  WHERE TIMESTAMP = SYSDATE`;
  return db.execute(query);
};
