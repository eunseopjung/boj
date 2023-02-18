import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())


def fx(a, b, c):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        return (fx(a, b//2, c)**2) % c
    else:
        return ((fx(a, b//2, c)**2)*a) % c


print(fx(A, B, C))
