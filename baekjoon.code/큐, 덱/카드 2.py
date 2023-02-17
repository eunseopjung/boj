import sys
input = sys.stdin.readline

n = int(input())
s = [i for i in range(1, n+1)]

cnt = 0
while len(s)-cnt != 1:
    cnt += 1
    if len(s) - cnt == 1:
        break
    s.append(s[cnt])
    cnt += 1

print(s[cnt])
