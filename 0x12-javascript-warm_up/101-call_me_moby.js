#!/usr/bin/node

exports.callMeMoby = function (x, theFunction){
  let counter = x;

  do{
    theFunction();
    counter--;
  }while (counter > 0)
}
