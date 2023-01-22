import sys
input = sys.stdin.readline

s = []


def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    for i in range(1, N+1):
        if len(s) == 0:
            s.append(i)
            dfs()
            s.pop()
        elif i not in s and s[len(s)-1] < i:
            s.append(i)
            dfs()
            s.pop()


N, M = map(int, input().split())
dfs()
