import sys
input = sys.stdin.readline


def binomial_coefficient(n, k, p):
    # n!을 계산
    fact_n = 1
    for i in range(1, n+1):
        fact_n = (fact_n * i) % p

    # k!을 계산
    fact_k = 1
    for i in range(1, k+1):
        fact_k = (fact_k * i) % p

    # (n-k)!을 계산
    fact_nk = 1
    for i in range(1, n-k+1):
        fact_nk = (fact_nk * i) % p

    # 분모를 계산
    denominator = (fact_k * fact_nk) % p

    # 분자와 분모를 나누어 이항계수를 계산
    numerator = fact_n
    denominator_inv = pow(denominator, p-2, p)  # 모듈러 역원 계산
    binom = (numerator * denominator_inv) % p

    return binom


n, k = map(int, input().split())
print(binomial_coefficient(n, k, 1000000007))
