import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
space = deque()
for _ in range(n):
    command = input().split()
    if command[0] == 'push_front':
        space.appendleft(command[1])
    elif command[0] == 'push_back':
        space.append(command[1])
    elif command[0] == 'pop_front':
        if space:
            print(space.popleft())
        else:
            print('-1')
    elif command[0] == 'pop_back':
        if space:
            print(space.pop())
        else:
            print('-1')
    elif command[0] == 'size':
        print(len(space))
    elif command[0] == 'empty':
        if space:
            print('0')
        else:
            print('1')
    elif command[0] == 'front':
        if space:
            print(space[0])
        else:
            print('-1')
    elif command[0] == 'back':
        if space:
            print(space[-1])
        else:
            print('-1')
