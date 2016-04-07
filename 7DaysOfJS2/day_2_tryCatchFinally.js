process.stdin.resume();
process.stdin.setEncoding("ascii");

process.stdin.on("data", (input) => {
  if (!this.input) this.input = "";

  this.input += input;
});

process.stdin.on("end", (input) => {
    tryCatch(eval(this.input));
});

function tryCatch (my_string) {
  try {
    var newStr = my_string.split(``).reverse().join(``);
    console.log(`Reversed string is : ${newStr}`);
  } catch (err) {
    console.log(`Error : ${err.message}`);
  } finally {
    console.log(`Type of my_string is : ${typeof my_string}`);
  }
}
