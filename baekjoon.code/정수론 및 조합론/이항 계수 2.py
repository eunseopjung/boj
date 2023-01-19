import sys
input = sys.stdin.readline


def fx(a):
    n = 1
    for i in range(1, a+1):
        n *= i
    return n


N, K = map(int, input().split())

print((fx(N) // fx(K) // fx(N-K)) % 10007)
