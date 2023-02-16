import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    m, idx = map(int, input().split())
    v = deque(map(int, input().split()))
    cnt = 0
    while True:
        if v[0] == max(v):
            cnt += 1
            if idx == 0:
                break
            v.popleft()
            idx -= 1
        else:
            v.append(v.popleft())
            if idx == 0:
                idx = len(v) - 1
            else:
                idx -= 1
    print(cnt)
