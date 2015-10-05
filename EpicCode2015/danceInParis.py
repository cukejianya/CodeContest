input1 = raw_input().split(" ")
K = int(input1[1])
boys = map(int, raw_input().split(" "))
boys.sort()
girls = map(int, raw_input().split(" "))
girls.sort()

groups = 0
while len(boys) > 0 and len(girls) > 0:
    if abs(boys[0]-girls[0]) <= K:
        groups += 1
        del boys[0]
        del girls[0]
    else:
        if (boys[0]-girls[0]) < 0:
            del boys[0]
        else:
            del girls[0]

print groups
