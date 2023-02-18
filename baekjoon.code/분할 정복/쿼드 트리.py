import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().strip())) for _ in range(n)]


def fx(x, y, N):
    color = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != paper[i][j]:
                print('(', end='')
                fx(x, y, N//2)
                fx(x, y+N//2, N//2)
                fx(x+N//2, y, N//2)
                fx(x+N//2, y+N//2, N//2)
                print(')', end='')
                return
    if color:
        print(1, end='')
        return
    else:
        print(0, end='')
        return


fx(0, 0, n)
