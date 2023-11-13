#!/usr/bin/node

const args = process.argv.slice(2); // Remove the first two elements from process.argv
const firstArg = args[0];

if (firstArg === undefined) {
  console.log("No argument");
} else {
  console.log(firstArg);
}
