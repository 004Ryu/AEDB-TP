const db = require("../config/db").connection;

module.exports.list = async () => {
  var conn;
  const res = [];
  try {
    conn = await db;
    const query = `SELECT DB_ID, INSTANCE_NUMBER,STARTUP_TIME, VERSION, DB_NAME, INSTANCE_NAME, PLATFORM_NAME, DB_UNIQUE_NAME, NUMBER_THREADS \
    FROM TRABALHOPDB.DATABASE_INSTANCE                                                                           \
    WHERE STARTUP_TIME = (SELECT MAX(STARTUP_TIME) FROM TRABALHOPDB.DATABASE_INSTANCE)`;
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
