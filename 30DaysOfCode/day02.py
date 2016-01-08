M = float(raw_input())
T = int(raw_input()) * .01 * M
X = int(raw_input()) * .01 * M

print "The final price of the meal is $%d." % (round(M + T + X))
