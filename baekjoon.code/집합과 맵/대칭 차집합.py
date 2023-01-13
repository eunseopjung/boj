# import sys
#
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
# a_list = list(map(int, input().split()))
# b_list = list(map(int, input().split()))
#
# a_dict = {}
# b_dict = {}
# cnt = 0
# for i in a_list:
#     a_dict[i] = 0
# for i in b_list:
#     if i not in a_dict.keys():
#         cnt += 1
#
# for i in b_list:
#     b_dict[i] = 0
# for i in a_list:
#     if i not in b_dict.keys():
#         cnt += 1
#
# print(cnt)


import sys

input = sys.stdin.readline

N, M = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
print(len(a-b)+len(b-a))
