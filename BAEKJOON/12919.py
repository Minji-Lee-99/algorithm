# A와 B 2
#

def bf(T):
    global flag
    if flag:
        return
    if S == T:
        flag = True
        return
    if len(T) == 0:
        return
    if T[-1] == 'A':
        bf(T[:-1])
    if T[0] == 'B':
        bf(T[1:][::-1])
    return


S = input()
T = input()


flag = False
bf(T)
print(int(flag))

