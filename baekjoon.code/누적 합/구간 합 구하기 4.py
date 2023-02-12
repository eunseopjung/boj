import sys
input = sys.stdin.readline


n, m = map(int, input().split())
number = list(map(int, input().split()))

for i in range(1, n):
    number[i] = number[i] + number[i-1]

for _ in range(m):
    i, j = map(int, input().split())
    if i == 1:
        print(number[j-1])
    else:
        print(number[j-1] - number[i-2])
