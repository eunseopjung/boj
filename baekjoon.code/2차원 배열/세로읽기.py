import sys
input = sys.stdin.readline

arr = [[] for _ in range(5)]
ans = [[] for _ in range(15)]

for i in range(5):
    arr[i] = list(input().strip())

for i in range(5):
    for j in range(len(arr[i])):
        ans[j].append(arr[i][j])

for i in range(len(ans)):
    for j in range(len(ans[i])):
        print(ans[i][j], end="")
