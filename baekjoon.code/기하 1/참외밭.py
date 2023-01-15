import sys
input = sys.stdin.readline

K = int(input().rstrip())

values = [input().split() for _ in range(6)]
d = [int(v[0]) for v in values]
l = [int(v[1]) for v in values]
max_l, box_l = [], []

for i in range(1, 5):
    if d.count(i) == 1:
        max_l.append(l[d.index(i)])
        tmp = d.index(i) + 3
        if tmp >= 6:
            tmp -= 6
        box_l.append(l[tmp])

area = max_l[0] * max_l[1] - box_l[0] * box_l[1]
print(K * area)
