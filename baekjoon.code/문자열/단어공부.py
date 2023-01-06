S = input("")
S = S.upper()
abc = 'abcdefghijklmnopqrstuvwxyz'.upper()
c = [0] * len(abc)

for k in S:
    c[abc.index(k)] += 1

m = max(c)
arr = [i for i, v in enumerate(c) if v == m]
if len(arr) > 1:
    print('?')
else:
    print(abc[c.index(max(c))])
