import math


prime_num = [True for _ in range(2 * 123456 + 1)]
prime_num[0], prime_num[1] = False, False

for i in range(2, int(math.sqrt(2*123456) + 1)):
    if prime_num[i]:
        j = 2
        while i * j <= 2 * 123456:
            prime_num[i * j] = False
            j += 1

while True:
    n = int(input())
    if n == 0:
        break

    cnt = 0
    for i in range(n + 1, 2 * n + 1):
        if prime_num[i]:
            cnt += 1
    print(cnt)
