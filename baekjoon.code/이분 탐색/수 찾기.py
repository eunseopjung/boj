import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
A.sort()


def fx(key):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == key:
            return mid
        if A[mid] > key:
            end = mid - 1
        else:
            start = mid + 1
    return -1


for i in B:
    if fx(i) == -1:
        print(0)
    else:
        print(1)
