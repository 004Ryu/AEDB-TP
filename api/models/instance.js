const db = require("../config/db").connection;

module.exports.list = () => {
  const query = `SELECT DB_ID, INSTANCE_NUMBER,STARTUP_TIME, VERSION, DB_NAME, INSTANCE_NAME, PLATFORM_NAME, DB_UNIQUE_NAME, NUMBER_THREADS \
  FROM DATABASE_INSTANCE                                                                           \
  WHERE STARTUP_TIME = (SELECT MAX(STARTUP_TIME) FROM DATABASE_INSTANCE)`;
  return db.execute(query);
};
