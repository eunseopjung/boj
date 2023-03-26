import sys
input = sys.stdin.readline

N = int(input())
D = 0
P = 0
for i in range(N):
    winner = input().strip()
    if winner == 'D':
        D += 1
    elif winner == 'P':
        P += 1
    if abs(D-P) == 2:
        break
print(str(D)+':'+str(P))
