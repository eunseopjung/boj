from collections import deque


def solution(progresses, speeds):
    answer = []
    p = deque(progresses)
    s = deque(speeds)
    while p:
        for i in range(len(p)):
            p[i] += s[i]
        cnt = 0
        while p:
            if p[0] >= 100:
                cnt += 1
                p.popleft()
                s.popleft()
            else:
                if cnt:
                    answer.append(cnt)
                break
        if len(p) == 0 and cnt != 0:
            answer.append(cnt)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))