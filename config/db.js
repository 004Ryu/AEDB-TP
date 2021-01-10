const oracledb = require("oracledb");

module.exports.connection = oracledb.getConnection({
  user: "system",
  password: "Oradoc_db1",
  connectString: "//127.0.0.1/orclpdb1.localdomain",
});
