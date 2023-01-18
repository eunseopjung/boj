import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

for i in range(1, len(li)):
    n = li[0]
    m = li[i]
    gcd = 0
    lcm = 0
    a = n
    b = m

    while True:
        c = a % b
        if c == 0:
            gcd = b
            break
        a, b = b, c

    print("{0}/{1}".format(n//gcd, m//gcd))
