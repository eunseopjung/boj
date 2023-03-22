import sys
input = sys.stdin.readline
from collections import deque


def bfs(graph, start):
    queue = deque()
    queue.append(start)
    if setNum[start] == 0:
        setNum[start] = 1

    while queue:
        v = queue.popleft()
        color = setNum[v]
        for i in graph[v]:
            if setNum[i] == 0:
                queue.append(i)
                if color == 1:
                    setNum[i] = 2
                else:
                    setNum[i] = 1
            elif setNum[i] == 1:
                if color == 1:
                    return False
            elif setNum[i] == 2:
                if color == 2:
                    return False
    return True


T = int(input())
for _ in range(T):
    flag = 0
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    setNum = [0 for _ in range(V + 1)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    for k in range(1, V + 1):
        if not bfs(graph, k):
            flag = 1
            break
    if flag == 0:
        print("YES")
    else:
        print("NO")
