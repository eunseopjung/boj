T = int(input())

for i in range(T):
    h, w, n = map(int, input().split())
    number = (n-1) // h + 1
    floor = (n-1) % h + 1
    if number < 10:
        print(floor, '0', number, sep='')
    else:
        print(floor, number, sep='')
