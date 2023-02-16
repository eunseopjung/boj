import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
order = list(map(int, input().split()))
q = deque(i for i in range(1, n+1))

cnt = 0
for i in order:
    while True:
        if q[0] == i:
            q.popleft()
            break
        if len(q)//2 < q.index(i):
            q.appendleft(q.pop())
            cnt += 1
        else:
            q.append(q.popleft())
            cnt += 1
print(cnt)
