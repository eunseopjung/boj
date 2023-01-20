import sys
input = sys.stdin.readline


def fx(a):
    n = 1
    for i in range(1, a+1):
        n *= i
    return n


N = int(input())
n = fx(N)

cnt = 0
while True:
    if n % 10:
        break
    else:
        n = n // 10
        cnt += 1

print(cnt)
