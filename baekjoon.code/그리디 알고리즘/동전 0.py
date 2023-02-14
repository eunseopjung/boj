import sys
input = sys.stdin.readline

n, k = map(int, input().split())

value = []
for i in range(n):
    value.append(int(input().strip()))

value.sort(reverse=True)

cnt = 0
for i in value:
    cnt += k // i
    k = k % i

print(cnt)
