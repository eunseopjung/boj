import sys
input = sys.stdin.readline

li_x = []
li_y = []
for i in range(3):
    x, y = map(int, input().split())
    li_x.append(x)
    li_y.append(y)

for i in range(3):
    if li_x.count(li_x[i]) == 1:
        ans_x = li_x[i]
    if li_y.count(li_y[i]) == 1:
        ans_y = li_y[i]

print(ans_x, ans_y)
