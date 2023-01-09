# A와 B 2
def bf(cnt_a, cnt_b, word, word_length):
    global flag
    if word == T:
        flag = True
        return
    elif cnt_a > target_cnt_a or cnt_b > target_cnt_b:
        return
    elif word_length >= target_length:
        return
    if flag:
        return
    bf(cnt_a + 1, cnt_b, word + 'A', word_length + 1)
    bf(cnt_a, cnt_b + 1, 'B' + word[::-1], word_length + 1)
    return


S = input()
T = input()

target_length = len(T)
target_cnt_a = T.count('A')
target_cnt_b = T.count('B')

flag = False
bf(S.count('A'), S.count('B'), S, len(S))
print(int(flag))

