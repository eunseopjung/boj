import sys


def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = (len(array) + 1) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    i, j, q = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[q] = left[i]
            ans.append(left[i])
            i += 1
        else:
            array[q] = right[j]
            ans.append(right[j])
            j += 1
        q += 1

    if i == len(left):
        while j < len(right):
            array[q] = right[j]
            ans.append(right[j])
            j += 1
            q += 1
    elif j == len(right):
        while i < len(left):
            array[q] = left[i]
            ans.append(left[i])
            i += 1
            q += 1
    return array


n, k = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
ans = []
merge_sort(num)

if len(ans) >= k:
    print(ans[k - 1])
else:
    print('-1')
