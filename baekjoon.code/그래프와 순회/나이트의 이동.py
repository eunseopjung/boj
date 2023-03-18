import sys
from collections import deque
input = sys.stdin.readline


def bfs(s, a):
    if s == a:
        return 0
    queue = deque()
    queue.append(s)

    while queue:
        x, y = queue.popleft()
        dx = [1, 2, 2, 1]
        dy = [2, 1, -1, -2]
        for i in range(4):
            for j in [1, -1]:
                nx = x + dx[i] * j
                ny = y + dy[i] * j
                if nx < 0 or nx >= l or ny < 0 or ny >= l:
                    continue
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
                    if (nx, ny) == a:
                        break
    return graph[a[0]][a[1]]


t = int(input())
for _ in range(t):
    l = int(input())
    startX, startY = map(int, input().split())
    arriveX, arriveY = map(int, input().split())
    graph = [[0 for _ in range(l)] for _ in range(l)]
    print(bfs((startX, startY), (arriveX, arriveY)))
