import sys
from collections import deque
input = sys.stdin.readline



def bfs(n, k):
    if n == k:
        return 0
    queue = deque()
    queue.append(n)

    while queue:
        x = queue.popleft()
        dx = [1, -1, x]
        for i in range(3):
            nx = x + dx[i]
            if nx < 0 or nx > 100000:
                continue
            if graph[nx] == 0:
                graph[nx] = graph[x]+ 1
                queue.append(nx)
                if nx == k:
                    break
    return graph[k]


n, k = map(int, input().split())
graph = [0] * (100000 + 1)

print(bfs(n, k))
