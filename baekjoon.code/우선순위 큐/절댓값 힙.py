# import sys
# import heapq
# input = sys.stdin.readline
#
# n = int(input())
# p = list()
# m = list()
#
# for i in range(n):
#     x = int(input())
#
#     if x == 0:
#         if len(p) + len(m) == 0:
#             print(0)
#         else:
#             if len(p) == 0 and len(m) > 0:
#                 print(-heapq.heappop(m))
#             elif len(p) > 0 and len(m) == 0:
#                 print(heapq.heappop(p))
#             else:
#                 if p[0] < m[0]:
#                     print(heapq.heappop(p))
#                 else:
#                     print(-heapq.heappop(m))
#     else:
#         if x > 0:
#             heapq.heappush(p, x)
#         else:
#             heapq.heappush(m, abs(x))


import sys
import heapq
input = sys.stdin.readline
# heapq에 튜플로 자료를 추가한다면 0번째 데이터만을 가지고 정렬을 한다

n = int(input())
heap = list()

for i in range(n):
    x = int(input())

    if x == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(x), x))
