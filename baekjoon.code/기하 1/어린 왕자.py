import sys
import math
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for cx, cy, r in li:
        d1 = math.sqrt((x1 - cx) ** 2 + (y1 - cy) ** 2)
        d2 = math.sqrt((x2 - cx) ** 2 + (y2 - cy) ** 2)
        if (d1 < r) ^ (d2 < r):
            ans += 1
    print(ans)
