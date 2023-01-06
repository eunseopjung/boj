N = int(input())

a = N // 5
b = N % 5

if N == 4 or N == 7:
    print('-1')
else:
    if b == 0:
        print(a)
    elif b == 1 or b == 3:
        print(a+1)
    else:
        print(a+2)
