# 보물상자 비밀번호

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    num = input()
    n = N // 4
    arr = set()
    for i in range(n):
        for j in range(0, N, n):
            arr.add(int('0x' + num[j:j+n], 16))
        num = num[N - 1] + num[:N - 1]
    arr = list(arr)
    arr.sort(reverse=True)
    print(f'#{tc} {arr[K - 1]}')
