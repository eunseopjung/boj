import sys
input = sys.stdin.readline

n, a = int(input()), list(map(int, input().split()))
stack = []
number = [0] * (1000000+1)
answer = [-1] * n
for i in a:
    number[i] += 1

stack.append(0)
for i in range(1, n):
    while stack and number[a[stack[-1]]] < number[a[i]]:
        answer[stack.pop()] = a[i]
    stack.append(i)

print(*answer)
