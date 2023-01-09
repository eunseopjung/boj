import sys

N = int(input())
li = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    li.append((x, y))

li.sort(key=lambda x: (x[1], x[0]))
for x, y in li:
    print(x, y)
