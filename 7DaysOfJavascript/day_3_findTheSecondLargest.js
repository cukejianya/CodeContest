Math.max.apply(null, myArray.filter(function(elm) {
  if (elm === Math.max.apply(null, myArray)) return false;

  return true;
}))
