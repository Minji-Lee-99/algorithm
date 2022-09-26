# 병합 정렬
def merge(left, right):
    global cnt
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        elif left[i] > right[j]:
            result.append(right[j])
            j += 1
    if i < len(left):
        result += left[i:]
        cnt += 1
    elif j < len(right):
        result += right[j:]
    return result


def mergesort(l, r):
    if r == l:
        return arr[l:l+1]
    else:
        mid = (l+r+1) // 2
        left = mergesort(l, mid - 1)
        right = mergesort(mid, r)
    return merge(left, right)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    sorted_arr = mergesort(0, N-1)
    print(f'#{tc} {sorted_arr[N // 2]} {cnt}')
