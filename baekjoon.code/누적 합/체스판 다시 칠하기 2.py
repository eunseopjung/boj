import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
board = []

for _ in range(n):
    board.append(input().strip())

prefix_sum = [[0 for col in range(m+1)]for row in range(n+1)]

for a in range(n):
    for b in range(m):
        value = 0
        if (a + b) % 2 == 0:
            if board[a][b] != 'B':
                value = 1
        else:
            if board[a][b] != 'W':
                value = 1
        prefix_sum[a+1][b+1] = prefix_sum[a+1][b] + prefix_sum[a][b+1] - prefix_sum[a][b] + value

cnt = []
for i in range(1, n - k + 2):
    for j in range(1, m - k + 2):
        cnt.append(prefix_sum[i+k-1][j+k-1] - prefix_sum[i+k-1][j-1] - prefix_sum[i-1][j+k-1] + prefix_sum[i-1][j-1])
        cnt.append(k**2 - cnt[len(cnt)-1])

print(min(cnt))

# import sys
#
# sys.maxsize
#
# # n, m, k 입력받기
# n, m, k = map(int, sys.stdin.readline().rstrip().split())
# # 보드 입력받아서 저장하기
# board = []
# for i in range(n):
#     str = list(sys.stdin.readline().rstrip())
#     board.append(str)
#
#
# # print(board)
#
# def chess(color):
#     prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]
#     for i in range(n):
#         for j in range(m):
#             if (i + j) % 2 == 0:
#                 value = board[i][j] != color
#             else:
#                 value = board[i][j] == color
#             prefix_sum[i + 1][j + 1] = prefix_sum[i][j + 1] + prefix_sum[i + 1][j] - prefix_sum[i][j] + value
#
#     count = sys.maxsize
#     for i in range(1, n - k + 2):
#         for j in range(1, m - k + 2):
#             count = min(count,
#                         prefix_sum[i + k - 1][j + k - 1] - prefix_sum[i + k - 1][j - 1] - prefix_sum[i - 1][j + k - 1] + prefix_sum[i - 1][j - 1])
#     return count
#
# print(min(chess('B'), chess('W')))
