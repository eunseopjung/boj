import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

result = []


def fx(x, y, N):
    color = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != paper[i][j]:
                fx(x, y, N//2)
                fx(x, y+N//2, N//2)
                fx(x+N//2, y, N//2)
                fx(x+N//2, y+N//2, N//2)
                return
    if color:
        result.append(1)
    else:
        result.append(0)


fx(0, 0, n)
print(result.count(0))
print(result.count(1))
