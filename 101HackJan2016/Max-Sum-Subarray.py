def find_max_sum(arr):
    arr = arr.split(' 0')
    there_is_max = False
    for sub_array in arr:
        sub_array = [int(x) for x in sub_array.split()]
        if not sub_array:
            if there_is_max:
                max_sum = max(0, max_sum)
            else:
                max_sum = 0
                there_is_max = True
            continue
        for i in range(len(sub_array)):
            for j in range(len(sub_array)-i):
                min_array = sub_array[i:i+j+1]

                total = reduce(lambda x, y: x+y, min_array)
                if there_is_max:
                    max_sum = max(total, max_sum)
                else:
                    max_sum = total
                    there_is_max = True

                print i, j, min_array, sub_array, max_sum

    return max_sum

n = raw_input()
array = raw_input()

print(find_max_sum(array))
