N = int(input())
c = 0
while 1:
    if c == 0:
        N = N - 1
        c += 1
    else:
        N = N - 6 * c
        c += 1
    if N <= 0:
        break
print(c)
