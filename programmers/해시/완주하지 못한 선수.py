def solution(participant, completion):
    di = {}
    for i in set(participant):
        di[i] = 0
    for i in completion:
        di[i] += 1
    for i in participant:
        if di[i] == 0:
            answer = i
            break
        else:
            di[i] -= 1
    return answer
