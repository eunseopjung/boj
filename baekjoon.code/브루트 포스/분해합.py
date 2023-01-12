def f(n, total=0):
    if len(str(n)) == 1:
        total += n
        return total
    total += n // (10**(len(str(n))-1))
    return f(n % (10**(len(str(n))-1)), total)


N = int(input())

for i in range(N):
    t = 0
    t = f(i, t) + i
    if t == N:
        print(i)
        break
    elif i == N-1:
        print(0)
