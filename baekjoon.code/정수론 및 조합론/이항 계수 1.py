import sys
input = sys.stdin.readline


def fx(a, b):
    if b:
        return fx(a - 1, b - 1) * a
    else:
        return 1


N, K = map(int, input().split())
numerator = fx(N, K)
denominator = fx(K, K)

print(numerator // denominator)
