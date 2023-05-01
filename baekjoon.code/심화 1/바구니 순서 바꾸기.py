import sys
input = sys.stdin.readline

n, m = map(int, input().split())
basket = [i+1 for i in range(n)]

for _ in range(m):
    i, j, k = map(int, input().split())
    temp = basket[k-1:j] + basket[i-1:k-1]
    basket[i-1:j] = temp

print(*basket)
