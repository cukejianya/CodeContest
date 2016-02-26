 process.stdin.resume();
 process.stdin.setEncoding("ascii");
 var log = console.log;
 process.stdin.on("on", (input) => {
   this.input = this.input || "";
   this.input += input;
 });

 process.stdin.on("end", () => processData(this.input));

 function processData(input) {
   input = input.split("\n");
   for(var turn of range(input.shift())) {
     console.log(find_minimum(input[turn]));
   }
 }

function range(num) {
  num = parseInt(num);
  return Array.call(null, Array(num)).map((elm, idx) => idx);
}

function find_minimum(word) {
  return null;
}
