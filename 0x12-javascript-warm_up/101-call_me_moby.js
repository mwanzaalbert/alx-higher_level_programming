#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  let counter = 0;

  do {
    theFunction();
    counter++;
  } while (counter < x);
};
