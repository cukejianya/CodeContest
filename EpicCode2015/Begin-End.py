N = int(raw_input())
S = raw_input()

dictRet = {}
for i in range(N):
    a = S[i]
    if a not in dictRet.keys():
        dictRet[a] = [1, 2]
    else:
        dictRet[a][0], dictRet[a][1]= dictRet[a][0]+dictRet[a][1], dictRet[a][1]+1

for k in dictRet:
     dictRet[k] = dictRet[k][0]

print sum(dictRet.itervalues())
