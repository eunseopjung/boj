import sys
input = sys.stdin.readline

n = int(input())
number = []
for _ in range(n):
    number.append(list(map(int, input().split())))
number.sort(key=lambda x: x[0])

dpF = [0] * n
for i in range(n):
    for j in range(i):
        if number[i][1] > number[j][1] and dpF[i] < dpF[j]:
            dpF[i] = dpF[j]
    dpF[i] += 1

print(n - max(dpF))
