def find_max_sum(arr):
    arr = arr.split(' 0')
    max_sum = 0
    for sub_array in arr:
        sub_array = [int(x) for x in sub_array.split()]
        best = current = 0
        for elm in sub_array:
            current = max(current + elm, 0)
            best = max(current, best)
            print 'elm:', elm, 'current:', current, 'best:', best, 'max_sum:', max_sum

        max_sum = max(max_sum, best)
    return max_sum

n = raw_input()
array = raw_input()

print(find_max_sum(array))
