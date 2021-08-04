#!/usr/bin/node

module.exports = {
  addMeMaybe: function (baseNum, func) {
    return (func(baseNum + 1));
  }
};
