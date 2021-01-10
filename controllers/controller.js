/* eslint-disable no-underscore-dangle */
const Instance = require("../models/instance");

module.exports.getInstances = async (req, res) => {
  res.jsonp(await Instance.list());
};
