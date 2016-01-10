input_num = [int(x) for x in raw_input().split()]
a = max(input_num[0], input_num[1])
b = min(input_num[0], input_num[1])

def gcd(a, b):
    r = a % b
    if r == 0:
        return b
    else:
        return gcd(b, r)

print gcd(a, b)
