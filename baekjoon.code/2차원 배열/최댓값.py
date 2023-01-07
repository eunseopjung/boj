M, N = 9, 9

a = [[0 for col in range(M)] for row in range(N)]

for i in range(N):
    a[i] = list(map(int, input().split()))

x, y = 0, 0
maximum = a[0][0]
for i in range(N):
    for j in range(M):
        if a[i][j] > maximum:
            maximum = a[i][j]
            x = i
            y = j
print(maximum)
print(x + 1, y + 1)
