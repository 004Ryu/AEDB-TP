const db = require("../config/db").connection;

module.exports.list = () => {
  const query = `SELECT SESSION_ID, SAMPLE_TIME, SQL_ID, SQL_OP_NAME, SQL_PLAN_OPERATION, WAIT_CLASS, WAIT_TIME, \
  SESSION_TYPE, SESSION_STATE, TIME_WAITED, TIMESTAMP, USER_ID \
  FROM SESSIONS S \
  INNER JOIN USERS U \
  ON U.USER_ID = S.USER_ID \
  WHERE TIMESTAMP = SYSDATE`;
  return db.execute(query);
};
