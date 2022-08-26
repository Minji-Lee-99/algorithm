# 자기 방으로 돌아가기

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    student = [list(map(int, input().split())) for _ in range(N)]
    length = 400 // 2
    cnt = [0] * (length + 1)
    max_cnt = 0
    for s in student:
        l, e = s[0] // 2 + s[0] % 2, s[1] // 2 + s[1] % 2
        for i in range(l, e + 1):
            cnt[i] += 1
            if cnt[i] > max_cnt:
                max_cnt = cnt[i]
    print(f'#{tc} {max_cnt}')

