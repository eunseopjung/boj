import sys

N = int(sys.stdin.readline())
numbers = sorted([int(sys.stdin.readline()) for _ in range(N)])

# 산술평균
print(round(sum(numbers) / N))

# 중앙값
print(numbers[N // 2])

# 최빈값
# 숫자, count로 리스트 만들기
count = []
for i in range(-4000, 4001):
    count.append([i, 0])
# num을 돌면서 해당 숫자를 표현하는 인덱스번호에 1을 추가해준다
for num in numbers:
    count[num + 4000][1] += 1
# 갯수 기준으로 정렬
count.sort(key=lambda x: (-x[1], x[0]))
# 출력
if N == 1:
    print(numbers[0])
else:
    if count[0][1] != count[1][1]:
        print(count[0][0])
    else:
        print(count[1][0])

# 범위 : 최댓값 - 최솟값
print(max(numbers) - min(numbers))
