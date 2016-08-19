import sys

sys.stdout = open('ans.out', 'w')

def find_jam_coins(n, j):
    i = 0
    gen_jamcoin = generate_coins(n)
    while i < j:
        jamcoin = gen_jamcoin.next()
        divisors = find_divisors(jamcoin)
        if not divisors:
            continue
        i += 1
        print jamcoin, " ".join(divisors)

def generate_coins(n):
    limit = bin_limit(n-2)
    for dec in range(limit + 1):
        bin_str = bin(dec)[2:]
        yield format_coin(bin_str, n-2)

def bin_limit(limit):
    max_bin = int('1'*limit)
    bin_str = '0b'+str(max_bin)
    return int(bin_str, 2)

def format_coin(str, length):
    padded_coin = str.zfill(length)
    return '1' + padded_coin + '1'

def find_divisors(jamcoin):
    divisors = []
    for x in range(2,11):
        dec_base = base(jamcoin, x)
        divisor = isNotPrime(dec_base)
        if not divisor:
            return False
        divisors.append(str(divisor))
    return divisors

def isNotPrime(base):
    for x in range(2, base):
        if (base % x == 0):
            return x
    return False

def base(coin, num):
    digit_array = list(coin)
    dec_base = 0
    for idx, digit in enumerate(digit_array[::-1]):
        dec_base += int(digit) * pow(num, idx)
    return dec_base

with open('input.in') as f:
    for idx, line in enumerate(f):
        if not idx:
            print "Case #1:"
            continue
        inp = map(int,line.split(" "))
        n, j = inp[0], inp[1]
    find_jam_coins(n, j)
