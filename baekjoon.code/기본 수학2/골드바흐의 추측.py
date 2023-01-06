# import math
#
# prime_num = [True for _ in range(10000 + 1)]
# prime_num[0], prime_num[1] = False, False
#
# for i in range(2, int(math.sqrt(10000) + 1)):
#     if prime_num[i]:
#         j = 2
#         while i * j <= 10000:
#             prime_num[i * j] = False
#             j += 1
#
# T = int(input())
# answer = []
# for j in range(T):
#     n = int(input())
#     cnt = 0
#     arr = [i for i, v in enumerate(prime_num) if i <= n and v is True]
#     for i in arr:
#         for k in arr:
#             if i + k == n:
#                 answer.append({i, k})
#     m = answer[0]
#     for i in range(len(answer)):
#         if m > answer[i]:
#             m = answer[i]
#     a, b = m
#     print('{0} {1}'.format(a, b))
#     answer.clear()


def isPrime(num):
    if num == 1:
        return False
    sq = int(num**0.5)
    for j in range(2, sq + 1):
        if num % j == 0:
            return False
    return True


for T in range(int(input())):
    num = int(input())
    a, b = num//2, num//2
    while a > 0:
        if isPrime(a) and isPrime(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1
