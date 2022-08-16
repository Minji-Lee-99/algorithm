T = int(input())
for tc in range(1, T + 1):
    A, B = input().split()
    i = cnt = 0
    while i <= len(A) - len(B):
        flag = True
        for j in range(len(B)):
            if A[i + j] != B[j]:
                flag = False
        if flag:
            cnt += 1
            i += len(B)
        else:
            i += 1
    print(f'#{tc} {len(A) - (len(B)-1) * cnt}')