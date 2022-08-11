# 이진탐색
def binary_search(P, target):
    l = 1 # 시작점
    r = P # 끝
    cnt = 0
    while l <= r:
        cnt += 1
        mid = (l + r) // 2
        if mid == target:
            return cnt
        elif mid < target:
            l = mid
        else:
            r = mid
    return -1


T = int(input())
for test_case in range(1, T + 1):
    P, A, B = map(int, input().split())
    cnt_A = binary_search(P, A)
    cnt_B = binary_search(P, B)
    if cnt_A == cnt_B:
        print(f'#{test_case} {0}')
    elif cnt_A < cnt_B:
        print(f'#{test_case} A')
    else:
        print(f'#{test_case} B')

