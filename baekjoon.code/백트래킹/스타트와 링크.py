# import sys
# input = sys.stdin.readline
#
# N = int(input())
# number = []
# for _ in range(N):
#     number.append(list(map(int, input().split())))
# tA = []
# tB = []
# minScore = int(1e9)
#
#
# def combi(arr):
#     result = []
#     for i in range(len(arr)):
#         for j in arr[i+1:]:
#             result.append((arr[i], j))
#     return result
#
#
# def statCheck(n):
#     global tA, tB
#     global minScore
#
#     # 팀을 2명씩 쌍으로 나누기, 팀점수 계산 후 최솟값 구하기
#     if len(tA) == N//2 and len(tB) == N//2:
#         a_list = combi(tA)
#         b_list = combi(tB)
#         a_score = 0
#         b_score = 0
#         for i, j in a_list:
#             a_score += number[i][j] + number[j][i]
#         for i, j in b_list:
#             b_score += number[i][j] + number[j][i]
#         if minScore > abs(a_score - b_score):
#             minScore = abs(a_score - b_score)
#         return
#
#     # 팀 나누기
#     for i in range(N):
#         if i not in tA and i not in tB:
#             if len(tA) != N//2:
#                 tA.append(i)
#                 statCheck(n+1)
#                 tA.pop()
#             if len(tB) != N//2:
#                 tB.append(i)
#                 statCheck(n + 1)
#                 tB.pop()
#
#
# statCheck(0)
# print(minScore)

import sys
input = sys.stdin.readline


def dfs(index):
    global minAns

    # 백트래킹 답 체크 시점
    if index == N // 2:
        startSum = 0
        linkSum = 0
        for i in range(0,N):
            if i not in start:
                link.append(i)
        for i in range(0, N // 2 - 1):
            for j in range(i+1, N // 2):
                startSum += arr[start[i]][start[j]] + arr[start[j]][start[i]]
                linkSum += arr[link[i]][link[j]] + arr[link[j]][link[i]]
        diff = abs(linkSum-startSum)
        if minAns > diff:
            minAns = diff
        # 링크팀을 항상 계산이 끝나면 비워줘야한다.
        link.clear()
        return

    #dfs 시행
    for i in range(N):
        if i in start:
            continue
        if len(start) > 0 and start[len(start)-1] > i:
            continue
        start.append(i)
        dfs(index + 1)
        start.pop()


N = int(input())

arr = []
start = []
link = []
for i in range(N):
    arr.append(list(map(int, input().split())))

minAns = float('Inf')
dfs(0)
print(minAns)
