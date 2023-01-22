import sys
input = sys.stdin.readline

# s = []
#
#
# def check(a, i):
#     if a == 0:
#         return 1
#     if s[a - 1] > i:
#         return 0
#     for j in range(a - 1):
#         if s[j] > s[j + 1]:
#             return 0
#     return 1
#
#
# def dfs():
#     if len(s) == M:
#         print(' '.join(map(str, s)))
#         return
#
#     for i in range(1, N+1):
#         if check(len(s), i):
#             s.append(i)
#             dfs()
#             s.pop()
#
#
# N, M = map(int, input().split())
# dfs()

s = []


def dfs(start):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    for i in range(start, N+1):
        s.append(i)
        dfs(i)
        s.pop()


N, M = map(int, input().split())
dfs(1)
