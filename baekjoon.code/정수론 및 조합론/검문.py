import sys
import math
input = sys.stdin.readline


def gcd(n, m):
    if n < m:
        n, m = m, n
    if m == 0:
        return n
    return gcd(m, n % m)


N = int(input())
ns = list(int(input()) for _ in range(N))
ns.sort()
interval = []
ans = []

for i in range(1, N):
    interval.append(ns[i] - ns[i - 1])

prev = interval[0]
for i in range(1, len(interval)):
    prev = gcd(prev, interval[i])

for i in range(2, int(math.sqrt(prev)) + 1):
    if prev % i == 0:
        ans.append(i)
        ans.append(prev//i)
ans.append(prev)
ans = list(set(ans))
ans.sort()
print(*ans)
