"use strict"

process.stdin.resume();
process.stdin.setEncoding("ascii");

process.stdin.on("data", (input) => {
  if (!this.input) this.input = "";

  this.input += input;
});

process.stdin.on("end", () => {
  var input = this.input.split(' ').map(num => parseInt(num));
  console.log(totalPressure.apply(null, input));
});
function totalPressure(g, m, h) {
  return pressure(g)(m)(h);
}

let pressure = (gravity) => (mass) => (height) => gravity * mass * height;
