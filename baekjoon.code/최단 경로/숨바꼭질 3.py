import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
import heapq

N, M = map(int, input().split())
INF = int(1e9)
distance = [INF] * (100000+1)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        dx = [1, -1, now]
        dy = [1, 1, 0]
        if distance[now] < dist:
            continue
        for i in range(3):
            if now + dx[i] > 100000 or now + dx[i] < 0:
                continue
            cost = dist + dy[i]
            if cost < distance[now + dx[i]]:
                distance[now + dx[i]] = cost
                heapq.heappush(q, (cost, now + dx[i]))


dijkstra(N)
print(distance[M])
