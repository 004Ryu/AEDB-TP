var createError = require("http-errors");
var express = require("express");
var path = require("path");
var logger = require("morgan");
const router = require("./routes/router.js");
const db = require("./config/db").connection;

var app = express();

app.use(logger("dev"));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(express.static(path.join(__dirname, "public")));

app.use("/", router);

async function testDBConn() {
  const dbTest = await db
    .then((conn) =>
      console.log(
        `Teste de conecção à Base de Dados bem sucedida: ${JSON.stringify(
          conn
        )}`
      )
    )
    .catch((err) => console.log(`Erro na conecção à Base de Dados: ${err}`));
}
testDBConn();

// const spawn = require("child_process").spawn;
// const pythonProcess = spawn("python", ["./agent_v3.py"]);

// No agent_v3.py deve existir o seguinte codigo para enviar mensagens para o servidor node
// print(dataToSendBack)
// sys.stdout.flush()

// pythonProcess.stdout.on("data", (data) => {
//   // Do something with the data returned from python script
// });

// catch 404 and forward to error handler
app.use(function (req, res, next) {
  next(createError(404));
});

// error handler
app.use(function (err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get("env") === "development" ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render("error");
});

module.exports = app;
