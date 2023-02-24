import sys
input = sys.stdin.readline

n, c = map(int, input().split())
x = [int(input()) for _ in range(n)]
x.sort()

start, end = 1, x[-1] - x[0]
ans = 0
while start <= end:
        mid = (start + end) // 2
        current = x[0]
        count = 1

        for i in range(1, len(x)):
            if x[i] >= current + mid:
                count += 1
                current = x[i]

        if count >= c:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1

print(ans)
