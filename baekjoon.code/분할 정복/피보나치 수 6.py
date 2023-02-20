import sys
input = sys.stdin.readline

n = int(input())
p = 1000000007


def mul(U, V):
    n = len(U)
    Z = [[0] * n for _ in range(n)]

    for row in range(n):
        for col in range(n):
            e = 0
            for i in range(n):
                e += U[row][i] * V[i][col]
            Z[row][col] = e % p

    return Z


def square(A, B):
    if B == 1:
        for x in range(len(A)):
            for y in range(len(A)):
                A[x][y] %= p
        return A

    tmp = square(A, B // 2)
    if B % 2:
        return mul(mul(tmp, tmp), A)
    else:
        return mul(tmp, tmp)


fib_matrix = [[1, 1], [1, 0]]
print(square(fib_matrix, n)[0][1])
