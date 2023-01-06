a, b, c = map(int, input().split())
d = c - b

if d <= 0:
    print('-1')
else:
    n = a / d
    n += 1
    print(int(n))
