import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
s = deque(i for i in range(1, n+1))
ans = []

while s:
    for i in range(k-1):
        s.append(s.popleft())
    ans.append(s.popleft())

print('<', end='')
print(*ans, sep=', ', end='')
print('>', end='')