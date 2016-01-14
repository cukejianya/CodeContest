def row(arr, idx, jdx):
    summation = 0
    for x in range(3):
        summation += arr[idx][jdx+x]
    return summation

def largest_hourglass(arr):
    for x in range(16):
        idx = x // 4
        jdx = x % 4
        abc = row(arr, idx, jdx)
        d = arr[idx+1][jdx+1]
        efg = row(arr, idx+2, jdx)
        total = abc + d + efg
        if x == 0:
            biggest = total
        else:
            biggest = max(biggest, total)
    return biggest

arr = []
for x in range(6):
    arr.append([int(x) for x in raw_input().split()])
print largest_hourglass(arr)
