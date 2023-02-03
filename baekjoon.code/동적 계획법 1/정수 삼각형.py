import sys
input = sys.stdin.readline

n = int(input())
li = []

for i in range(n):
    li.append(list(map(int, input().split())))

for i in range(n-1, -1, -1):
    for j in range(i):
        li[i-1][j] = li[i-1][j] + max(li[i][j], li[i][j+1])

print(li[0][0])
