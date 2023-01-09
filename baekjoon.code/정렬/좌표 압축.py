N = int(input())

li = list(map(int, input().split()))

a = list(set(li))
a.sort()

numdict = {}
for i in range(len(a)):
    numdict[a[i]] = i

for i in li:
    print(numdict[i], end=' ')
