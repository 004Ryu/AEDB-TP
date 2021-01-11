/* eslint-disable no-underscore-dangle */
const Cpu = require("../models/cpu");
const Datafiles = require("../models/datafiles");
const Instance = require("../models/instance");
const Memory = require("../models/memory");
const Profiles = require("../models/profiles");
const Roles = require("../models/roles");
const Sessions = require("../models/sessions");
const Tablespaces = require("../models/tablespaces");
const UserHasRoles = require("../models/userHasRoles");
const Users = require("../models/users");

module.exports.getCPU = async (req, res) => {
  res.jsonp(await Cpu.list());
};

module.exports.getDatafiles = async (req, res) => {
  res.jsonp(await Datafiles.list());
};

module.exports.getInstance = async (req, res) => {
  res.jsonp(await Instance.list());
};

module.exports.getMemory = async (req, res) => {
  res.jsonp(await Memory.list());
};

module.exports.getProfiles = async (req, res) => {
  res.jsonp(await Profiles.list());
};

module.exports.getRoles = async (req, res) => {
  res.jsonp(await Roles.list());
};

module.exports.getSessions = async (req, res) => {
  res.jsonp(await Sessions.list());
};

module.exports.getTablespaces = async (req, res) => {
  res.jsonp(await Tablespaces.list());
};

module.exports.getUserHasRoles = async (req, res) => {
  res.jsonp(await UserHasRoles.list());
};

module.exports.getUsers = async (req, res) => {
  res.jsonp(await Users.list());
};
