process.stdin.resume();
process.stdin.setEncoding("ascii");

process.stdin.on("data", (input) => {
  if (!this.input) this.input = "";
  this.input += input;
});

process.stdin.on("end", () => {
  processData(this.input.split(" ").map(num => parseInt(num)));
});

function processData(array) {
  console.log(myFilter(array, onlyEvens));
}

function myFilter(array, cb) {
  return array.reduce((prev, curr) => {
    if (cb(curr)) {
      prev.push(curr);
    }
    return prev;
  },[])
}

function onlyEvens(num) {
  if (num % 2 === 0) {
    return true;
  } else {
    return false;
  }
}
