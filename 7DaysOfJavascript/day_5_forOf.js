for(var word of my_array) {
  if (word === reverse(word)) {
    console.log(word);
  }
}

function reverse(str) {
  return str.split("").reverse().join("")
}
