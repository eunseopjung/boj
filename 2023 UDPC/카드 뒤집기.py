from collections import deque
import sys
input = sys.stdin.readline



def bfs(s):
    graph = [0] * (N + 1)
    queue = deque()
    queue.append(s)
    graph[s] = 1

    while queue:
        x = queue.popleft()
        dx = [x, -x]
        for i in range(2):
            a = x + dx[i]
            if a < 1 or a > N:
                continue
            if graph[a] == 0:
                graph[a] = graph[x] + 1
                queue.append(a)
    return graph


N = int(input())
for i in range(1, N+1):
    graph = bfs(i)
    print(graph)
