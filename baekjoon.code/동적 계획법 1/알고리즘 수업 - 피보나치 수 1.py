import sys
input = sys.stdin.readline


def fib(n):
    global cnt1
    if n == 1 or n == 2:
        cnt1 += 1
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fibonacci(n):
    global cnt2
    global dp
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
        cnt2 += 1


n = int(input())
dp = [0 for _ in range(n)]
dp[0] = 0
dp[1] = 1
cnt1 = 0
cnt2 = 0

fib(n)
fibonacci(n)
print(cnt1, cnt2)
