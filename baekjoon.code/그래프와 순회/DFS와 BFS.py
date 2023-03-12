import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
ansD = [0] * (n + 1)
ansB = [0] * (n + 1)
cntD = 1
cntB = 1
queue = deque()

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n + 1):
    graph[i].sort()


def dfs(R):
    global cntD
    ansD[R] = cntD
    print(R, end=' ')
    for i in graph[R]:
        if not ansD[i]:
            cntD += 1
            dfs(i)


def bfs(R):
    global cntB
    ansB[R] = cntB
    print(R, end=' ')
    queue.append(R)
    while queue:
        u = queue.popleft()
        for i in graph[u]:
            if not ansB[i]:
                cntB += 1
                ansB[i] = cntB
                print(i, end=' ')
                queue.append(i)


dfs(v)
print()
bfs(v)
