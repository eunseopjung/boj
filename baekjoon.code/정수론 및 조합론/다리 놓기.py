import sys
input = sys.stdin.readline


def fx(a):
    n = 1
    for i in range(1, a+1):
        n *= i
    return n


T = int(input())

for i in range(T):
    n, m = map(int, input().split())
    bridge = fx(m) // (fx(n) * fx(m-n))
    print(bridge)
