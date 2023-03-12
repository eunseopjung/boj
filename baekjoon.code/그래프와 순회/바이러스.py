import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m = int(input()), int(input())
graph = [[] for _ in range(n + 1)]
ans = [0] * (n + 1)
cnt = 1

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(R):
    global cnt
    ans[R] = cnt
    for i in graph[R]:
        if not ans[i]:
            cnt += 1
            dfs(i)


dfs(1)
virus = 0
for i in range(2, n+1):
    if ans[i]:
        virus += 1
print(virus)
