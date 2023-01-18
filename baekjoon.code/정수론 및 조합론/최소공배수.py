import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
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

    lcm = n * m // gcd
    print(lcm)
