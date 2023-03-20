import sys
from collections import deque
input = sys.stdin.readline


def bfs(s):
    queue = deque()
    queue.append(s)
    while queue:
        x = queue.popleft()
        dx = [1, 2, 3, 4, 5, 6]
        for i in range(6):
            nx = x + dx[i]
            if nx < 0 or nx > 100 or graph[nx] != 0:
                continue
            if nx in ladder.keys():
                nx = ladder[nx]
            if nx in snake.keys():
                nx = snake[nx]
            if graph[nx] == 0:
                queue.append(nx)
                graph[nx] = graph[x] + 1
    return graph[100]


n, m = map(int, input().split())
graph = [0] * (100 + 1)

snake = dict()
ladder = dict()
for _ in range(n):
    a, b = map(int, input().split())
    ladder[a] = b
for _ in range(m):
    a, b = map(int, input().split())
    snake[a] = b

print(bfs(1))
