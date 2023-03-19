import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs():
    queue = deque()
    for z in range(h):
        for i in range(m):
            for j in range(n):
                if graph[z][i][j] == 1:
                    queue.append((z, i, j))

    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if nz < 0 or nz >= h or nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[z][x][y] + 1
                queue.append((nz, nx, ny))

    maxV = 0
    for z in range(h):
        for i in range(m):
            for j in range(n):
                if graph[z][i][j] == 0:
                    return -1
                else:
                    if maxV < graph[z][i][j]:
                        maxV = graph[z][i][j]
    return maxV - 1


n, m, h = map(int, input().split())
graph = []
for j in range(h):
    floor = []
    for i in range(m):
        floor.append(list(map(int, input().split())))
    graph.append(floor)

print(bfs())
