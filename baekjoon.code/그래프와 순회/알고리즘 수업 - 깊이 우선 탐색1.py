import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
ans = [0] * (n + 1)
cnt = 1

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(n + 1):
    graph[i].sort()


def dfs(R):
    global cnt
    ans[R] = cnt
    for i in graph[R]:
        if not ans[i]:
            cnt += 1
            dfs(i)


dfs(r)
for i in range(1, n+1):
    print(ans[i])
