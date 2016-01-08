from math import pow

T = int(raw_input())
for x in range(T):
    input_list = raw_input().split()
    input_list = [int(x) for x in input_list]
    a = input_list[0]
    b = input_list[1]
    N = input_list[2]
    array = []
    for idx in range(N):
        a += (pow(2, idx) * b)
        array.append(a)
    print " ".join(str(int(x)) for x in array)
