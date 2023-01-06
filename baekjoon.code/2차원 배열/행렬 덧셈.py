N, M = map(int, input().split())

a = [[0 for col in range(M)] for row in range(N)]

for i in range(N):
    a[i] = list(map(int, input().split()))

b = [[0 for col in range(M)] for row in range(N)]

for i in range(N):
    b[i] = list(map(int, input().split()))

c = [[0 for col in range(M)] for row in range(N)]

for i in range(N):
    for j in range(M):
        c[i][j] = a[i][j] + b[i][j]

for i in c:
    for j in i:
        print(j, end=' ')
    print()
