import sys
input = sys.stdin.readline

n = int(input())
space = []
cnt = 0
for _ in range(n):
    command = input().split()
    if command[0] == 'push':
        space.append(command[1])
    elif command[0] == 'pop':
        if len(space) > cnt:
            print(space[cnt])
            cnt += 1
        else:
            print('-1')
    elif command[0] == 'size':
        print(len(space)-cnt)
    elif command[0] == 'empty':
        if len(space) == cnt:
            print('1')
            space = []
            cnt = 0
        else:
            print('0')
    elif command[0] == 'front':
        if len(space) > cnt:
            print(space[cnt])
        else:
            print('-1')
    elif command[0] == 'back':
        if len(space) > cnt:
            print(space[-1])
        else:
            print('-1')
