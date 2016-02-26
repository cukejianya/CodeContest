 process.stdin.resume();
 process.stdin.setEncoding("ascii");
 var log = console.log;
 process.stdin.on("data", (input) => {
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
  return Array.apply(null, Array(num)).map((elm, idx) => idx);
}

function find_minimum(word) {
  var operations = 0;
  var wordLength = word.length;
  var half = Math.floor(wordLength / 2);
  for (var i = 0; i < half; i++) {
    if(word[i] !== word[wordLength - i - 1]) {
      operations += Math.abs(
        word.charCodeAt(i) - word.charCodeAt(wordLength - i - 1)
      );
    }
  }
  return operations;
}
