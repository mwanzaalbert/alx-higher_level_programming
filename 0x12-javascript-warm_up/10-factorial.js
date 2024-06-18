#!/usr/bin/node

const x = Number.parseInt(process.argv[2]);

function fact (mynumber) {
  if (Number.isNaN(mynumber)) return 1;

  switch (mynumber) {
    case 0:
    case 1:
      return 1;
    default:
      return mynumber * fact(mynumber - 1);
  }
}

console.log(fact(x));
