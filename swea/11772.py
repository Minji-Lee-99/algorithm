# 이진탐색
def bs(key):
    l, r = 0, N - 1
    mid = (l + r) // 2
    if A[mid] == key:
        return True
    elif A[mid] < key:
        l = mid + 1
        before = 1
    else:
        r = mid - 1
        before = 0
    while l <= r:
        mid = (l + r) // 2
        if A[mid] == key:
            return True
        elif A[mid] < key:
            if before == 0:
                l = mid + 1
                before = 1
            else:
                break
        elif A[mid] > key:
            if before == 1:
                r = mid - 1
                before = 0
            else:
                break
        else:
            break
    return False


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    cnt = 0
    for b in B:
        if bs(b):
            cnt += 1
    print(f'#{tc} {cnt}')
