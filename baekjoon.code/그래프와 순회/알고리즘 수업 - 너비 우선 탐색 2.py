import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
ans = [0] * (n + 1)
cnt = 1

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(n + 1):
    graph[i].sort(reverse=True)

queue = deque()


def bfs(R):
    global cnt
    ans[R] = cnt
    queue.append(R)
    while queue:
        u = queue.popleft()
        for i in graph[u]:
            if not ans[i]:
                cnt += 1
                ans[i] = cnt
                queue.append(i)


bfs(r)
for i in range(1, n+1):
    print(ans[i])
