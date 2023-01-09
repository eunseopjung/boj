N = int(input())

li = []
for i in range(N):
    age, name = input().split()
    age = int(age)
    li.append((age, name))

li.sort(key=lambda x: x[0])

for i, j in li:
    print(i, j)
