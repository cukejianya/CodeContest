def find_max_sum(arr):
    arr = arr.split(' 0 ')
    for idx, sub_array in enumerate(arr):
        
        for elm in sub_array:
            total = reduce(lambda x, y: x+y, [int(x) for x in sub_array.split()])
            if idx == 0:
                max_sum = total
            else:
                max_sum = max(total, max_sum)

    return max_sum

n = raw_input()
array = raw_input()

print(find_max_sum(array))
