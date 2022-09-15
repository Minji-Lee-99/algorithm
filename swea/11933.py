# 노드의 합
def postorder(n):
    if n <= size:
        if tree[n] == 0:
            tree[n] = postorder(2 * n) + postorder(2 * n + 1)
        return tree[n]
    return 0


T = int(input())
for tc in range(1, T + 1):
    size, M, L = map(int, input().split())
    tree = [0] * (size + 1)
    for _ in range(M):
        a, b = map(int, input().split())
        tree[a] = b
    postorder(1)
    print(f'#{tc} {tree[L]}')
