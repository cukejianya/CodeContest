def binaryConversion(dec):
    new_dec = dec // 2
    r = dec % 2
    if new_dec == 0:
        return str(r)

    return binaryConversion(new_dec) + str(r)

T = int(raw_input())
for x in range(T):
    dec = int(raw_input())
    print binaryConversion(dec)
