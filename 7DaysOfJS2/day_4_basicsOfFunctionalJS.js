process.stdin.resume();
process.stdin.setEncoding("ascii");

process.stdin.on("data", (input) => {
  if (!this.input) this.input = "";

  this.input = input;
});

process.stdin.on("end", () => {
  input = this.input;
  processData(Number(input));
});

function processData(input) {
  var waterWeight = multiplier(1);
  var mercuryWeight = multiplier(1.355);
  var oilWeight = multiplier(0.900);

  console.log("Weight of " + input + " metric cube of water = " + waterWeight(input) + " kg");
  console.log("Weight of " + input + " metric cube of mercury = " + mercuryWeight(input) + " kg");
  console.log("Weight of " + input + " metric cube of oil = " + oilWeight(input) + " kg");
}

function multiplier(x) {
  return y => (x * y);
}
