import sys
input = sys.stdin.readline

num = int(input())
factor = list(map(int, input().split()))
factor.sort()
print(factor[-1] * factor[0])
