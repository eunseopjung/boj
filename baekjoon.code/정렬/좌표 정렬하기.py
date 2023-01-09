import sys

N = int(input())
li = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    li.append((x, y))

li.sort(key=lambda x: (x[0], x[1]))
for x, y in li:
    print(x, y)
