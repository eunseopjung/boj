N = int(input())
num = []
num.extend(map(int, input().split()))
total = 0
a = 0
for i in num:
    for j in range(1, i + 1):
        if i % j == 0:
            a += 1
    if i != 1 and a <= 2:
        total += 1
    a = 0
print(total)
