process.stdin.resume();
process.stdin.setEncoding();

process.stdin.on("data", (input) => {
  if (!this.input) this.input = "";
  this.input += input;
});

process.stdin.on("end", () => {
  try_catch(this.input);
});

function try_catch(input) {
  try {
    if (isNaN(input)) {
      throw new Error("notANumberError");
      console.log(input);
    } else {
      if (input > 10) throw new Error("hugeHeightError");
      if (input < 4) throw new Error("tinyHeightError");
    }
    console.log(input);
  } catch (err) {
    console.log(err.message);
  }


}
