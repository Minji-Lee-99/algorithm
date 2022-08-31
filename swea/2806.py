# N-Queen
#백트래킹

def bt(k):
    global cnt
    if k == N:
        cnt += 1
        return
    else:
        for j in range(N):
            flag = True
            for i in range(k):
                if abs(i - k) == abs(col[i] - j) or col[i] == j:
                    flag = False
                    break
            if flag:
                col[k] = j
                bt(k + 1)
    return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    col = [0] * N
    cnt = 0
    bt(0)
    print(f'#{tc} {cnt}')
