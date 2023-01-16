import sys
import math
input = sys.stdin.readline

r = int(input())

print(round(math.pi * r * r, 6))
print(round(pow(2 * r, 2) / 2, 6))
