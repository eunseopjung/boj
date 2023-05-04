import sys
input = sys.stdin.readline

rating = {"A+": 4.5, "A0": 4, "B+": 3.5, "B0": 3, "C+": 2.5, "C0": 2, "D+": 1.5, "D0": 1, "F": 0}

total_b = 0
total_bc = 0
for _ in range(20):
    a, b, c = input().split()
    if c in rating.keys():
        total_b += float(b)
        total_bc += float(b)*rating[c]
print("{0:0.6f}".format(total_bc/total_b))
