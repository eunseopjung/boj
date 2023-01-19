import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())

    di = {}
    for i in range(n):
        a, b = input().split()
        if b in di.keys():
            di[b] += 1
        else:
            di[b] = 1

    ans = 1
    for i in di.values():
        ans *= i + 1

    print(ans - 1)
    di.clear()
