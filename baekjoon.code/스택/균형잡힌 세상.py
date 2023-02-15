import sys
input = sys.stdin.readline

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


while True:
    vs = input().rstrip()
    if vs == '.':
        break
    for i in range(len(vs)):
        if vs[i] in '()[]':
            push(vs[i])
            if len(stack) >= 2:
                if stack[-1] == ')' and stack[-2] == '(':
                    pop()
                    pop()
                    continue
                if stack[-1] == ']' and stack[-2] == '[':
                    pop()
                    pop()
    if len(stack):
        print('NO')
    else:
        print('YES')
    stack.clear()
