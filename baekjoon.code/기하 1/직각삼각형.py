import sys
input = sys.stdin.readline

li = []
while True:
    n = list(map(int, input().split()))
    if n == [0, 0, 0]:
        break
    else:
        li.append(n)

for i in range(len(li)):
    li[i].sort()
    if li[i][0]**2 + li[i][1]**2 == li[i][2]**2:
        print("right")
    else:
        print("wrong")
