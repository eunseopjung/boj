import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
import heapq

n, m = map(int, input().split())
k = int(input())
INF = int(1e9)
graph = [[] * (n+1) for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(k)
for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])



# import sys
# from collections import deque
# input = sys.stdin.readline
#
#
# def bfs(start, end):
#     if start == end:
#         return 0
#     queue = deque()
#     queue.append((start, 0))
#     minV = 1e9
#
#     # s:시작지점 value:가치총합 e:끝지점 w:가중치
#     while queue:
#         s, value = queue.popleft()
#         for e, W in graph[s]:
#             if e == end:
#                 minV = min(value + W, minV)
#             elif e < end:
#                 queue.append((e, value + W))
#     if minV == 1e9:
#         return "INF"
#     else:
#         return minV
#
#
# V, E = map(int, input().split())
# K = int(input())
# graph = [[] for _ in range(V+1)]
# for _ in range(E):
#     u, v, w = map(int, input().split())
#     graph[u].append([v, w])
#
# for i in range(1, V+1):
#     print(bfs(K, i))
