const express = require("express");

const router = express.Router();

/** Importação dos controladores necessários:
 *      Post: controlador correspondente à informação dos posts presentes na plataforma;
 */
const Controller = require("../controllers/controller");

/** @method get : Otenção da informação da tabela CPU.
 */
router.route("/cpu").get(Controller.getCPU);

/** @method get : Otenção da informação da tabela Datafiles.
 */
router.route("/datafiles").get(Controller.getDatafiles);

/** @method get : Otenção da informação da tabela Database_Instance.
 */
router.route("/instances").get(Controller.getInstance);

/** @method get : Otenção da informação da tabela Memory.
 */
router.route("/memory").get(Controller.getMemory);

/** @method get : Otenção da informação da tabela Profiles.
 */
router.route("/profiles").get(Controller.getProfiles);

/** @method get : Otenção da informação da tabela Roles.
 */
router.route("/roles").get(Controller.getRoles);

/** @method get : Otenção da informação da tabela Sessions.
 */
router.route("/sessions").get(Controller.getSessions);

/** @method get : Otenção da informação da tabela Tablespaces.
 */
router.route("/tablespaces").get(Controller.getTablespaces);

/** @method get : Otenção da informação da tabela UserHasRoles.
 */
router.route("/userhasroles").get(Controller.getUserHasRoles);

/** @method get : Otenção da informação da tabela Users.
 */
router.route("/users").get(Controller.getUsers);

module.exports = router;
