var input_arr = [];

process.stdin.on("data", input => {input_arr.push(parseInt(input))})

var my_function = arr => arr.map( num => { if (num%2 === 0) {return ++num} return --num });
