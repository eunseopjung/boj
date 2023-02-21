def solution(nums):
    s = set(nums)
    if len(s) >= len(nums)//2:
        answer = len(nums)//2
    else:
        answer = len(s)
    return answer


nums = [[3,1,2,3],
[3,3,3,2,2,4],
[3,3,3,2,2,2]]
for i in nums:
    print(solution(i))
