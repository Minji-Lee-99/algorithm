# subtree
def inorder(n):
    if n:
        return inorder(ch1[n]) + 1 + inorder(ch2[n])
    else:
        return 0


T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    ch1 = [0] * (E + 2)
    ch2 = [0] * (E + 2)
    temp = list(map(int, input().split()))
    for i in range(E):
        a, b = temp[2 * i], temp[2 * i + 1]
        if ch1[a] == 0:
            ch1[a] = b
        else:
            ch2[a] = b
    print(f'#{tc} {inorder(N)}')

