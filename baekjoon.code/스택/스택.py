import sys
input = sys.stdin.readline

n = int(input())
stack = []


def push(x):
    global stack
    stack.append(x)
    return


def pop():
    global stack
    if len(stack):
        print(stack[-1])
        stack.pop()
    else:
        print('-1')
    return


def size():
    global stack
    print(len(stack))
    return


def empty():
    global stack
    if len(stack):
        print(0)
    else:
        print(1)
    return


def top():
    global stack
    if len(stack):
        print(stack[-1])
    else:
        print(-1)


for _ in range(n):
    command = input().split()
    if command[0] == 'push':
        push(command[1])
    elif command[0] == 'pop':
        pop()
    elif command[0] == 'size':
        size()
    elif command[0] == 'empty':
        empty()
    else:
        top()
