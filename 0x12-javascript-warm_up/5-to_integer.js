#!/usr/bin/node

const newArgs = process.argv.slice(2);
const firstArg = newArgs[0];

if (!isNaN(firstArg)) {
  const n = parseInt(firstArg);
  console.log(`My number: ${n}`);
} else {
  console.log('Not a number');
}
