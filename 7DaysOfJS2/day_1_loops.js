var str = process.argv[2];

console.log(str.split("").filter(function(elm) {
  if ("aeiou".indexOf(elm) !== -1) {
    console.log(elm);
    return false;
  } else {
    return true;
  }
}).join("\n"));
