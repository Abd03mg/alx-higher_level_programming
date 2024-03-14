#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const lis = process.argv.slice(2).sort(function (a, b) { return b - a; }).reverse();
  console.log(lis[1]);
}
