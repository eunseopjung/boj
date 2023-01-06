word = input('')
initial = ['c', 'd', 'l', 'n', 's', 'z']
special_case = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
total = 0

for i in range(len(word)):
    if word[i] in initial:
        if word[i:i+2] in special_case:
            continue
        elif word[i:i+3] == 'dz=':
            continue
        else:
            total += 1
    else:
        total += 1
print(total)
