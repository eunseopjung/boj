N = input()

num = [0] * 10
for i in N:
    num[int(i)] += 1

for i in range(9, -1, -1):
    if num[i] != 0:
        for j in range(num[i]):
            print(i, end='')
