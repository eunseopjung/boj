import sys
input = sys.stdin.readline

s = []


def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    for i in range(1, N+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()


N, M = map(int, input().split())
dfs()
