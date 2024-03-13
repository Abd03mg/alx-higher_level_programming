#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  const counter = parseInt(process.argv[2]);
  for (let i = 0; counter > i; i++) {
    for (let j = 0; counter > j; j++) {
      process.stdout.write('X');
    } console.log('');
  }
}
