import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
import heapq


def dijkstra(start):
    q = []
    distance = [INF] * (n+1)
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
    return distance


T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    INF = int(1e9)
    graph = [[] * (n+1) for _ in range(n+1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    end = []
    for _ in range(t):
        end.append(int(input()))
    end.sort()
    for i in end:
        one = dijkstra(s)
        v1_ = dijkstra(g)
        v2_ = dijkstra(h)
        cnt = min(one[g] + v1_[h] + v2_[i], one[h] + v2_[g] + v1_[i])
        if cnt == one[i]:
            print(i, end=' ')
    print()
