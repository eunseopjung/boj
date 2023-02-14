import sys
input = sys.stdin.readline

n = int(input())
length = list(map(int, input().split()))
price = list(map(int, input().split()))

ans = 0
minPrice = price[0]
for i in range(1, n):
    ans += minPrice * length[i - 1]
    if minPrice > price[i]:
        minPrice = price[i]

print(ans)
