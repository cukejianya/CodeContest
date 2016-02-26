function christmasTree(num) {
  console.log(" ".repeat(num-1) + "*");
  for (var i = 0; i < num; i++) {
    console.log(" ".repeat(num-i-1) + "0".repeat(1+i*2));
  }
}

christmasTree(9);
