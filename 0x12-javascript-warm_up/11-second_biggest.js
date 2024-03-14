#!/usr/bin/node
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  const lis = process.argv.slice(2, process.argv.length).sort().reverse();
  console.log(lis[1]);
}
