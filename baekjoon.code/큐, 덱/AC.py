from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    command = input().strip()
    n = int(input())
    num = input()
    q = deque()
    v = True
    cnt = 0
    if n:
        q = deque(map(int, num[1:-2].split(sep=',')))
    for c in command:
        if c == 'R':
            cnt += 1
        else:
            if q:
                if cnt % 2:
                    q.pop()
                else:
                    q.popleft()
            else:
                print('error')
                v = False
                break
    if cnt % 2 == 1:
        q.reverse()
    if v:
        print('[', end='')
        print(*q, sep=',', end='')
        print(']')
