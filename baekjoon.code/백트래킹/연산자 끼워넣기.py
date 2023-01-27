import sys
input = sys.stdin.readline

n = int(input())
number = list(map(int, input().split()))
operator = list(map(int, input().split()))
minV = int(1e9)
maxV = -int(1e9)

ans = number[0]


def dfs(idx):
    global ans, maxV, minV

    if idx == n:
        if ans > maxV:
            maxV = ans
        if ans < minV:
            minV = ans
        return

    for i in range(4):
        tmp = ans
        if operator[i] > 0:
            if i == 0:
                ans += number[idx]
            elif i == 1:
                ans -= number[idx]
            elif i == 2:
                ans *= number[idx]
            else:
                if ans >= 0:
                    ans //= number[idx]
                else:
                    ans = (-ans // number[idx] * -1)

            operator[i] -= 1
            dfs(idx+1)
            ans = tmp
            operator[i] += 1


dfs(1)
print(maxV)
print(minV)