#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
Object.defineProperty(myObject, "incr", function () {
  myObject.value += 1
})
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);