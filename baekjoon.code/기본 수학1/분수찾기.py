x = int(input())
c = 1

while 1:
    if x - c > 0:
        x = x - c
        c += 1
    else:
        y = c+1-x
        x = x
        if c % 2 == 0:
            print("{0}/{1}".format(x, y))
            break
        else:
            print("{1}/{0}".format(x, y))
            break
