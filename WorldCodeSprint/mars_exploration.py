def message_decode(msg):
    arr = [check(msg[i:i+3]) for i in range(0, len(msg), 3) if msg[i:i+3] != 'SOS']
    return len("".join(arr))

def check(sub):
    newstr = ""
    for i,x in enumerate('SOS'):
        if x != sub[i]:
            newstr += sub[i]
    return newstr

print message_decode(raw_input())
