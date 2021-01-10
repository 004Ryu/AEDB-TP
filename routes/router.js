const express = require("express");

const router = express.Router();

/** Importação dos controladores necessários:
 *      Post: controlador correspondente à informação dos posts presentes na plataforma;
 */
const Controller = require("../controllers/controller");

/** @method get : Otenção da informação da tabela Database_Instance.
 */
router.route("/instances").get(Controller.getInstances);

module.exports = router;
