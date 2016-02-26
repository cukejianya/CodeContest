function generateWave(num) {
  return "\u2571\u2572".repeat(num);
}

function waves(num) {
  for (var i = 0; i < num*2; i++) {
    console.log(generateWave(num));
  }
}

waves(7);
