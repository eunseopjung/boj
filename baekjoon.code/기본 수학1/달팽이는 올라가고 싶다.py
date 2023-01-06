# import math
#
# a, b, v = map(int, input().split())
# d = a - b
# n = math.ceil(v / d)
# if v - (a * (n-b)) + (b * (n-b-1)) <= 0:
#     n = n - b
# print(int(n))

A, B, V = map(int, input().split())

days = ((V - B - 1) // (A - B)) + 1

print(days)
