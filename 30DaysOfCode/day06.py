n = int(raw_input())

for idx in range(1, n+1):
    arr = [" " for x in range(n-idx)] + ["#" for x in range(idx)]
    print "".join(arr)
