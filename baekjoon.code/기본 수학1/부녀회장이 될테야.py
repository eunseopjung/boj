T = int(input())


for i in range(T):
    k = int(input())
    n = int(input())
    apart = [0] * n
    new_apart = [0] * n
    total = 0
    for j in range(n):
        apart[j] = j+1
    for k in range(k):
        total = 0
        for j in range(n):
            total = total + apart[j]
            new_apart[j] = total
        for j in range(n):
            apart[j] = new_apart[j]
    print(apart[n-1])
