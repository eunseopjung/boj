def solution(nums):
    s = set(nums)
    if len(s) >= len(nums)//2:
        answer = len(nums)//2
    else:
        answer = len(s)
    return answer
