def group_word(w):
    seen_chars = set()
    for i, c in enumerate(w):
        if c in seen_chars and word[i - 1] != c:
            return False
        seen_chars.add(c)
    return True


N = int(input())
cnt = 0

for j in range(N):
    word = input()
    if group_word(word):
        cnt += 1
print(cnt)
