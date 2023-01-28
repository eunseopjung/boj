import sys
input = sys.stdin.readline

N = int(input())
number = []
for _ in range(N):
    number.append(list(map(int, input().split())))
tA = []
tB = []
minScore = int(1e9)


def combi(arr):
    result = []
    for i in range(len(arr)):
        for j in arr[i+1:]:
            result.append((arr[i], j))
    return result


def statCheck(n):
    global tA, tB
    global minScore

    # 팀을 2명씩 쌍으로 나누기, 팀점수 계산 후 최솟값 구하기
    if len(tA) == N//2 and len(tB) == N//2:
        a_list = combi(tA)
        b_list = combi(tB)
        a_score = 0
        b_score = 0
        for i, j in a_list:
            a_score += number[i][j] + number[j][i]
        for i, j in b_list:
            b_score += number[i][j] + number[j][i]
        if minScore > abs(a_score - b_score):
            minScore = abs(a_score - b_score)
        return

    # 팀 나누기
    for i in range(N):
        if i not in tA and i not in tB:
            if len(tA) != N//2:
                tA.append(i)
                statCheck(n+1)
                tA.pop()
            if len(tB) != N//2:
                tB.append(i)
                statCheck(n + 1)
                tB.pop()


statCheck(0)
print(minScore)
