import sys
input = sys.stdin.readline

n = int(input())
time = []
for i in range(n):
    time.append(list(map(int, input().split())))

cnt = 0
prev = 0
time.sort(key=lambda x: (x[1], x[0]))
for start, end in time:
    if start >= prev:
        cnt += 1
        prev = end

print(cnt)
