import sys
input = sys.stdin.readline

n = input().strip()

minus = n.split('-')

for i in range(len(minus)):
    total = 0
    plus = minus[i].split('+')
    for j in plus:
        total += int(j)
    minus[i] = total

ans = minus[0]
for i in range(1, len(minus)):
    ans -= minus[i]

print(ans)
