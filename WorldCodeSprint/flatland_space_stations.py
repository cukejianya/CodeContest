def maximum(arr, n):
    init_best = max(arr[0] - 0, n - arr[len(arr) - 1])
    best = 0
    for idx, num in enumerate(arr[1::]):
        prev = arr[idx]
        best = max(best, num-prev)
        print idx, num, arr, prev, best, n

    return max(init_best, best // 2)

n = int(raw_input().split()[0])
c = sorted(map(int,raw_input().strip().split(' ')))

print maximum(c, int(n)-1);
