#!/usr/bin/node
exports.converter = function (base) {
  function convertNumberToAnyBase (numberToConvert) {
    return numberToConvert.toString(base);
  }
  return convertNumberToAnyBase;
};
