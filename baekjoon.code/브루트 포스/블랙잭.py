import sys

N, M = map(int, input().split())
li = list(map(int, sys.stdin.readline().split()))
ans = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            s = li[i] + li[j] + li[k]
            if s > M:
                continue
            ans = max(ans, s)
print(ans)
