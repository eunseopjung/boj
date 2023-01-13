import sys

input = sys.stdin.readline

N = int(input().rstrip())
num = list(map(int, input().split()))

M = int(input().rstrip())
li = list(map(int, input().split()))
find = {value: 0 for i, value in enumerate(set(li))}

for i in num:
    if i in find.keys():
        find[i] += 1

for i in li:
    print(find[i], end=' ')
