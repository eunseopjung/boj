# import sys
# sys.setrecursionlimit(10**6)
#
#
# def paint_star(l):
#     DIV3 = l//3
#     if l == 3:
#         g[1] = ['*', ' ', '*']
#         g[0][:3] = g[2][:3] = ['*']*3
#         return
#
#     paint_star(DIV3)
#
#     for i in range(0, l, DIV3):
#         for j in range(0, l, DIV3):
#             if i != DIV3 or j != DIV3:
#                 for k in range(DIV3):
#                     g[i+k][j:j+DIV3] = g[k][:DIV3]
#
#
# n = int(sys.stdin.readline().strip())
# g = [[' ' for _ in range(n)] for _ in range(n)]
#
# paint_star(n)
#
# for i in range(n):
#     for j in range(n):
#         print(g[i][j], end='')
#     print()
import sys

sys.setrecursionlimit(10 ** 6)


def append_star(q):
    if q == 1:
        return ['*']

    stars = append_star(q // 3)
    l = []

    for s in stars:
        l.append(s * 3)
    for s in stars:
        l.append(s + ' ' * (q // 3) + s)
    for s in stars:
        l.append(s * 3)
    return l


n = int(sys.stdin.readline().strip())
print('\n'.join(append_star(n)))
