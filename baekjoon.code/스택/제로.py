import sys
input = sys.stdin.readline

k = int(input())
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


for _ in range(k):
    n = int(input())
    if n:
        push(n)
    else:
        pop()

print(sum(stack))
