import sys

N, M = map(int, sys.stdin.readline().split())

di = {}
for i in range(1, N+1):
    a = sys.stdin.readline().strip()
    di[i] = a
    di[a] = i

for i in range(M):
    q = sys.stdin.readline().strip()
    if q.isdigit():
        print(di[int(q)])
    else:
        print(di[q])
