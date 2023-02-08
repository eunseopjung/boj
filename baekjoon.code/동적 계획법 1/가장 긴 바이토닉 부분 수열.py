import sys
input = sys.stdin.readline

n = int(input())
number = list(map(int, input().split()))
dpF = [0] * n
for i in range(n):
    for j in range(i):
        if number[i] > number[j] and dpF[i] < dpF[j]:
            dpF[i] = dpF[j]
    dpF[i] += 1

dpB = [0] * n
for i in range(-1, -n-1, -1):
    for j in range(-1, i-1, -1):
        if number[i] > number[j] and dpB[i] < dpB[j]:
            dpB[i] = dpB[j]
    dpB[i] += 1

li = []
for i in range(n):
    li.append(dpF[i] + dpB[i])

print(max(li) - 1)
