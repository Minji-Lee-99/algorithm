# 파스칼의 삼각형

# 교수님이 알려주신 방법
# 미리 10까지 계산해서 메모에 저장해두기
SIZE = 100
memo = [[0] * SIZE for _ in range(SIZE)]
for i in range(SIZE):
    for j in range(i + 1):
        if i == j or j == 0:
            memo[i][j] = 1
        else:
            memo[i][j] = memo[i - 1][j - 1] + memo[i - 1][j]
# 입력된 값에 따라 출력
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}')
    for i in range(N):
        for j in range(i + 1):
            print(memo[i][j], end=' ')
        print('\n', end='')
    print('\n', end='')

# 내가 푼 방법
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [1]
#     print(f'#{tc}')
#     for i in range(N):
#         print(*arr)
#         arr = [0] + arr + [0]
#         arr = [arr[j] + arr[j + 1] for j in range(len(arr) - 1)]
