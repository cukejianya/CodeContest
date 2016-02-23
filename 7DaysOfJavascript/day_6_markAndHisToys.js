function processData(input) {
    //Enter your code here
    var input = input.split("\n").map((arr) => arr.split(" ").map(num => parseInt(num)));
    var k = input[0][1];
    var list = input[1].sort((a,b) => a - b);
    var sum = 0;
    var amount = 0;
    for (var num of list) {
        sum += num;
        if (sum <= k) {
            amount++;
        } else {
            break;
        }
    }
    console.log(amount);
}
