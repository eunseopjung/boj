import sys
input = sys.stdin.readline

N = int(input())
N//=4
for i in range(N):
    print("long", end=' ')
print("int")
