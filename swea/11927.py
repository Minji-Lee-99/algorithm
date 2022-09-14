# 이진탐색
def inorder(n):
    global num
    if n <= size:
        inorder(2 * n)
        tree[n] = num
        num += 1
        inorder(2 * n + 1)


T = int(input())
for tc in range(1, T + 1):
    size = int(input())
    tree = [0] * (size + 1)
    num = 1
    inorder(1)
    print(f'#{tc} {tree[1]} {tree[int(size/2)]}')
