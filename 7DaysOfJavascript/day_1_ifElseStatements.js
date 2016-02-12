var marks = Math.ceil(parseInt(process.argv[2])/10);
var ans = "";
switch(marks) {
  case 10:
    ans = "AA";
    break;
  case 9:
    ans = "AB";
    break;
  case 8:
    ans = "BB";
    break;
  case 7:
    ans = "BC";
    break;
  case 6:
    ans = "CC";
    break;
  case 5:
    ans = "CD";
    break;
  case 4:
    ans = "DD"
    break;
  default:
    ans = "FF"
}

console.log(ans);
