word = input('')
li = list(word)
abc = 'ABC DEF GHI JKL MNO PQRS TUV WXYZ'
num = abc.split(' ')
total = 0

for i in li:
    for j in num:
        if i in j:
            total += num.index(j) + 3
print(total)
