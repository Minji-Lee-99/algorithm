# 중위순회
def inorder(n):
    global ans
    if n <= V:
        inorder(n * 2)
        ans += tree[n]
        inorder(n * 2 + 1)


for tc in range(1, 11):
    V = int(input())
    tree = [0] * (V + 1)
    for _ in range(V):
        temp = input().split()
        tree[int(temp[0])] = temp[1]
    ans = ''
    inorder(1)
    print(f'#{tc} {ans}')
