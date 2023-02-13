import sys
input = sys.stdin.readline

n, m = map(int, input().split())
number = list(map(int, input().split()))

remainder = [0] * m
remainder[0] = 1

prefix_sum = 0
for i in range(n):
    prefix_sum += number[i]
    remainder[prefix_sum % m] += 1

ans = 0
for i in remainder:
    ans += i * (i-1) // 2

print(ans)
