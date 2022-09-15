# tree 이진힙

def enque(i, num):
    tree[i] = num
    p = i // 2
    while p > 0:
        if tree[p] > tree[i]:
            tree[p], tree[i] = tree[i], tree[p]
            i = p
            p = i // 2
        else:
            break
    return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    tree = [0] * (N + 1)
    for i in range(1, N + 1):
        enque(i, arr[i - 1])
    ans = 0
    p = N // 2
    while p > 0:
        ans += tree[p]
        p = p // 2
    print(f'#{tc} {ans}')
