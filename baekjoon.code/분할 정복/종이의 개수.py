# import sys
# input = sys.stdin.readline
#
# n = int(input())
# paper = [list(map(int, input().split())) for _ in range(n)]
# result = []
#
#
# def fx(x, y, N):
#     color = paper[x][y]
#     for i in range(x, x+N):
#         for j in range(y, y+N):
#             if color != paper[i][j]:
#                 fx(x, y, N//3)
#                 fx(x+N//3, y, N//3)
#                 fx(x+N//3*2, y, N//3)
#                 fx(x, y+N//3, N//3)
#                 fx(x, y+N//3*2, N//3)
#                 fx(x+N//3, y+N//3, N//3)
#                 fx(x+N//3*2, y+N//3, N//3)
#                 fx(x+N//3, y+N//3*2, N//3)
#                 fx(x+N//3*2, y+N//3*2, N//3)
#                 return
#     if color == 1:
#         result.append(1)
#     elif color == 0:
#         result.append(0)
#     else:
#         result.append(-1)
#
#
# fx(0, 0, n)
# print(result.count(-1))
# print(result.count(0))
# print(result.count(1))


import sys


def dfs(x, y, z):
    global answer
    visited = graph[x][y]

    # 반복문을 통해 종이를 확인
    for i in range(x, x + z):
        for j in range(y, y + z):
            # 시작점에 종이의 수가 현재 종이의 수와 다르다면
            if graph[i][j] != visited:
                # 3 * 3 범위를 재귀적으로 탐색
                for k in range(3):
                    for l in range(3):
                        dfs(x + k * z // 3, y + l * z // 3, z // 3)
                return

    # 카운트
    if visited == -1:
        answer[0] += 1
    elif visited == 0:
        answer[1] += 1
    else:
        answer[2] += 1


n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = [0, 0, 0]
dfs(0, 0, n)
[print(res) for res in answer]

