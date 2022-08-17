#파스칼의 삼각형

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [1]
    print(f'#{tc}')
    for i in range(N):
        print(*arr)
        arr = [0] + arr + [0]
        arr = [arr[j] + arr[j + 1] for j in range(len(arr) - 1)]