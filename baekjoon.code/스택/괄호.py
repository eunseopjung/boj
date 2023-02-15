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
        stack.pop()
    return


for _ in range(n):
    vs = input().strip()
    for i in range(len(vs)):
        push(vs[i])
        if len(stack) >= 2:
            if stack[-1] == ')' and stack[-2] == '(':
                pop()
                pop()
    if len(stack):
        print('NO')
    else:
        print('YES')
    stack.clear()
