import sys

input = sys.stdin.readline

N, M = map(int, input().split())

a = []
for i in range(N):
    a.append(input().rstrip())

b = []
for i in range(M):
    b.append(input().rstrip())

di = {}
for i in b:
    di[i] = 0

li = []
for i in a:
    if i in di.keys():
        li.append(i)

print(len(li))
li.sort()
for i in li:
    print(i)
