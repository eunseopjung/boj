M = int(input())
N = int(input())
a = 0
total = 0
num = []
prime_num = []

for i in range(M, N+1):
    num.append(i)

for i in num:
    for j in range(1, i + 1):
        if i % j == 0:
            a += 1
    if i != 1 and a <= 2:
        prime_num.append(i)
    a = 0

if prime_num:
    minimum = prime_num[0]
    for i in prime_num:
        if i < minimum:
            minimum = i
    for j in range(len(prime_num)):
        total += prime_num[j]
    print(total)
    print(minimum)
else:
    print('-1')
