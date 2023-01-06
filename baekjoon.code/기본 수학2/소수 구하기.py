import math


def isPrime(num):
    if num == 1:
        return False

    sq = int(math.sqrt(num))

    for j in range(2, sq + 1):
        if num % j == 0:
            return False
    return True


M, N = map(int, input().split())
for i in range(M, N + 1):
    if isPrime(i):
        print(i)
