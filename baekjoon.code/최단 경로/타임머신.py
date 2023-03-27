import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

INF = float('inf')
V, E = map(int, input().split())
edges = []
for _ in range(E):
    s, d, w = map(int, input().split())
    edges.append((s, d, w))


def bellmanford(start):
    dist = [INF] * (V + 1)
    dist[start] = 0
    for i in range(V):
        for s, d, w in edges:
            if dist[s] != INF and dist[d] > dist[s] + w:
                if i == V - 1:
                    return -1
                dist[d] = dist[s] + w
    return dist


ans = bellmanford(1)
if ans != -1:
    for i in range(2, V+1):
        if ans[i] == INF:
            print(-1)
        else:
            print(ans[i])
else:
    print(ans)
