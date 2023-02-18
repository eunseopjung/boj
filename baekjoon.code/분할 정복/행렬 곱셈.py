import sys

input = sys.stdin.readline

n, m = map(int, input().split())
num1 = []
for _ in range(n):
    num1.append(list(map(int, input().split())))

m, k = map(int, input().split())
num2 = []
for _ in range(m):
    num2.append(list(map(int, input().split())))

ans = [[0 for _ in range(k)] for _ in range(n)]
for N in range(n):
    for K in range(k):
        for M in range(m):
            ans[N][K] += num1[N][M] * num2[M][K]

for i in range(n):
    for j in range(k):
        print(ans[i][j], end=' ')
    print()
