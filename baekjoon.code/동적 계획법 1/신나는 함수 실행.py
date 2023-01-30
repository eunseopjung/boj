# import sys
# input = sys.stdin.readline
#
#
# def w():
#     global ans
#     for a in range(-50, 51):
#         for b in range(-50, 51):
#             for c in range(-50, 51):
#                 if a <= 0 or b <= 0 or c <= 0:
#                     ans[(a, b, c)] = 1
#                 elif a > 20 or b > 20 or c > 20:
#                     ans[(a, b, c)] = 1048576
#                 else:
#                     ans[(a, b, c)] = ans[(a-1, b, c)] + ans[(a-1, b-1, c)] + ans[(a-1, b, c-1)] - ans[(a-1, b-1, c-1)]
#     return
#
#
# abc = []
# while True:
#     a, b, c = map(int, input().split())
#     if a == b == c == -1:
#         break
#     abc.append([a, b, c])
#
# ans = dict()
# w()
# for a, b, c in abc:
#     print('w({}, {}, {}) = {}'.format(a, b, c, ans[(a, b, c)]))

import sys
input = sys.stdin.readline


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if dp[a][b][c]:
        return dp[a][b][c]
    if a < b < c:
        dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return dp[a][b][c]

    dp[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    return dp[a][b][c]


dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]

while True:
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    if a == -1 and b == -1 and c == -1:
        break
    ans = w(a, b, c)
    print("w(%d, %d, %d) = %d" % (a, b, c, ans))
