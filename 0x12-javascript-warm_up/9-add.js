#!/usr/bin/node
function add (a, b) {
  if (isNaN(a)) {
    return NaN;
  }
  return parseInt(a) + parseInt(b);
}

console.log(add(process.argv[2], process.argv[3]));
