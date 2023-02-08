import sys
input = sys.stdin.readline

n = int(input())
li = [0]
for _ in range(n):
    li.append(int(input()))
dp = [0, li[1]]
if n > 1:
    dp.append(li[1] + li[2])

for i in range(3, n + 1):
    dp.append(max(dp[i-3] + li[i-1] + li[i], dp[i-2] + li[i], dp[i-1]))

print(dp[n])
