const db = require("../config/db").connection;

module.exports.list = () => {
  const query = `SELECT USER_ID, USERNAME, ACCOUNT_STATUS, EXPIRY_DATE, DEFAULT_TABLESPACE, TEMPORARY_TABLESPACE, CREATED, \
  COMMON, LAST_LOGIN, TIMESTAMP, PROFILE_ID \
  FROM USERS \
  INNER JOIN PROFILES P \
  ON USERS.PROFILE_ID = P.PROFILE_ID \
  WHERE TIMESTAMP = SYSDATE AND LAST_LOGIN = SYSDATE`;
  return db.execute(query);
};
