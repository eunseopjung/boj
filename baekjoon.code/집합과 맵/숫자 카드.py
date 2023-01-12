import sys

n1 = int(input())
m1 = list(map(int, sys.stdin.readline().split()))
n2 = int(input())
m2 = list(map(int, sys.stdin.readline().split()))
s1 = set(m1)
s2 = set(m2)

li = [0] * 20000001
for i in s1:
    if i in s2:
        li[i] = 1

for i in m2:
    print(li[i], end=' ')

# import sys
#
# n = int(input())
# card = list(map(int, sys.stdin.readline().split()))
# m = int(input())
# check = list(map(int, sys.stdin.readline().split()))
#
# card.sort()
#
# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return None
#
#
# for i in range(m):
#     if binary_search(card, check[i], 0, n - 1) is not None:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')
