N = int(input())

li = []
for i in range(N):
    li.append(list(map(int, input().split())))

ans = []
for i in range(N):
    count = 0
    for j in range(N):
        if li[i][0] < li[j][0] and li[i][1] < li[j][1]:
            count += 1
    ans.append(count + 1)

for k in ans:
    print(k, end=' ')
