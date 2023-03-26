import sys
input = sys.stdin.readline

candidate = input().strip()
UC = 0
DP = 0
for i in candidate:
    if i in 'UC':
        UC += 1
    elif i in 'DP':
        DP += 1
if UC == 0 and DP == 0:
    print('C')
elif UC > 0 and DP == 0:
    print('U')
elif UC <= (DP + 1)//2:
    print('DP')
else:
    print('UDP')
