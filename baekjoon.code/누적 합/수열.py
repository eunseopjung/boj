import sys
input = sys.stdin.readline

n, k = map(int, input().split())
temp = list(map(int, input().split()))

prefix_sum = [sum(temp[:k])]

for i in range(n - k):
    prefix_sum.append(prefix_sum[i] - temp[i] + temp[i+k])

print(max(prefix_sum))
