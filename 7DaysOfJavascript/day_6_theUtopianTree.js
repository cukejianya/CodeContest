process.stdin.resume();
process.stdin.setEncoding('ascii');

process.stdin.on('data', function (data) {
  if(!this.input) {this.input = "";}
  this.input += data;
});

process.stdin.on('end', function () {
  var input = this.input.split("\n").map((num) => parseInt(num));
  main(input)
})

function main(arr) {
  arr.shift();
  for (var num of arr) {
    console.log(find_height(num));
  }
}

function find_height(cycles) {
  height = 1;
  for (var cycle of range(cycles)) {
    if (cycle%2) { height++; } else { height *= 2; }
  }
  return height;
}

function range(length){
  return Array.apply(null, Array(length)).map((elm, idx) => idx);
}
