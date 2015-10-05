input1 = raw_input()
input2 = raw_input()
N = int(input1.split(" ")[0])
P = int(input1.split(" ")[1])
X = int(input1.split(" ")[2])
A = input2.split(" ")
dictRet = {}

for i in range(N):
    dictRet[i+1] = P*int(A[i])
    P=P-X

print max(dictRet, key=dictRet.get)
