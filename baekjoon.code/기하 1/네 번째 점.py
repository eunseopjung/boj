import sys
input = sys.stdin.readline

x = []
y = []
for i in range(3):
    x, y = map(int, input().split())
    x.append(x)
    y.append(y)

for i in range(3):
    if x.count(x[i]) == 1:
        print(x[i], end=" ")
    if y.count(y[i]) == 1:
        print(y[i])
