
process.stdin.on("data", (input) => {  if(!this.input) { this.input = ""; }

  this.input += input;
});

process.stdin.on("end", () => {
  var input = this.input.split("\n").slice(2).map(
    (arr) => arr.split(" ").map((num) => parseInt(num))
  );

   findLargestRegion(input);
});

function findLargestRegion(matrix) {
  //console.log(matrix);
  var areas = [];
  var matrixTemplate = JSON.parse(JSON.stringify(matrix));
  matrixTemplate.forEach((elm, i) => {
    var row = matrixTemplate[i];
    for (var j in row) {
      j = parseInt(j);
      //console.log(typeof(j));
      if (matrix[i][j]) {
        matrix[i][j] = 0;
        areas.push(connectedCells(i, j, matrix, 1));
      }
    }
  });
  console.log(areas.sort((a, b) => b - a)[0]);
}

function connectedCells(i, j, matrix, area) {
  var max_y = matrix.length;
  var max_x = matrix[0].length;
  var x,y;
  for (var deg = 0; deg < 360; deg++) {
    x = j + Math.round(Math.cos(deg*45));
    y = i + Math.round(Math.sin(deg*45));
    //console.log("before:",x,y);
    if (boundryValidation(x, y, max_x, max_y)) {
      if (matrix[y][x]) {
        matrix[y][x] = 0;
        //console.log(matrix.join("\n"));
        //console.log(x,y);
        area += connectedCells(y,x,matrix, 1);
      }
    }

  }
  return area;
}

function boundryValidation(x, y, max_x, max_y) {
  xValidation = (x > -1 && x < max_x);
  yValidation = (y > -1 && y < max_y);

  return xValidation && yValidation;
}
