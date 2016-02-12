function sortLibrary(arr) {
  arr.sort(function(a, b) {
    return a.title.localeCompare(b.title);
  })
}
