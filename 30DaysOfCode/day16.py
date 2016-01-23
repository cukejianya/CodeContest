def min_abs_diff(arr):
    arr = sorted([int(x) for x in arr])
    pairs = []
    for idx, elm in enumerate(arr[:len(arr)-1:]):
        nxt = arr[idx+1]
        diff = abs(elm - nxt)
        if idx == 0:
            min_diff = diff
            pairs += [elm, nxt]
        else:
            if diff <= min_diff:
                if diff < min_diff:
                    pairs = []
                    min_diff = diff
                pairs += [elm, nxt]
    return pairs

n = raw_input()
arr = raw_input().split()

for x in min_abs_diff(arr):
    print x,
