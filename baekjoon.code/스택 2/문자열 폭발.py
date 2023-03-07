# import sys
# input = sys.stdin.readline
#
# sen = input().strip()
# bomb = list(input().strip())
# stack = []
#
# for i in sen:
#     stack.append(i)
#     if len(stack) >= len(bomb):
#         if stack[len(stack)-len(bomb):] == bomb:
#             for j in range(len(bomb)):
#                 stack.pop()
# if stack:
#     print(''.join(map(str, stack)))
# else:
#     print("FRULA")

n,k,a=list(input())[::-1],list(input()),[]
l=-len(k)
while n:
 a+=[n.pop()]
 if a[l:]==k:del a[l:]
print(''.join(a) if a else 'FRULA')
