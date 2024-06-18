#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  if (x <= 0) return;
  let counter = 0;

  do {
    theFunction();
    counter++;
  } while (counter < x);
};
