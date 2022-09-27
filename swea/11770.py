# quick sort
def partition(l, r):
    pivot = l
    i, j = l + 1, r
    while i <= j:
        while i <= j and arr[i] <= arr[pivot]:
            i += 1
        while i <= j and arr[j] >= arr[pivot]:
            j -= 1
        if i < j:   # 마직막에 i, j가 역전된 경우는 정렬이 끝난 것이고, pivot과 정렬해야 함.
            arr[i], arr[j] = arr[j], arr[i]
    arr[pivot], arr[j] = arr[j], arr[pivot]
    return j  # 반환값: pivot의 인덱스 값


def qs(l, r):
    if l < r:
        s = partition(l, r)
        qs(l, s - 1)
        qs(s + 1, r)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    qs(0, N - 1)
    print(f'#{tc} {arr[N//2]}')
