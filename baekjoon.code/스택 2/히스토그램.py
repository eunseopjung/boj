import sys
input = sys.stdin.readline

n = int(input())
hist = [0] * n
for i in range(n):
    hist[i] = int(input())

stack = []
max_area = 0
for i in range(n+1):
    while stack and (i == n or hist[stack[-1]] > hist[i]):
        height = hist[stack.pop()]
        width = i if not stack else i - stack[-1] - 1
        max_area = max(max_area, height*width)

    stack.append(i)

print(max_area)
