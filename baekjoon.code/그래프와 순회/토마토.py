import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    queue = deque()
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    maxV = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 0:
                return -1
            else:
                if maxV <= graph[i][j]:
                    maxV = graph[i][j]
    return maxV - 1


n, m = map(int, input().split())
graph = []
for i in range(m):
    graph.append(list(map(int, input().split())))

print(bfs())
