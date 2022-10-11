# 정수 삼각형
# 특정 노드까지의 최대누적합은 해당 부모노드들의 누적합 중 가장 큰 값에 해당 노드의 값을 더해준 값이다.
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
memo = [[0] * n for _ in range(n)]
memo[0][0] = arr[0][0]
for i in range(1, n):
    for j in range(i + 1):
        if j == 0:  # 연결된 부모노드가 1개인 경우
            memo[i][j] = memo[i - 1][j] + arr[i][j]
        elif j == i:  # 연결된 부모노드가 1개인 경우
            memo[i][j] = memo[i - 1][j - 1] + arr[i][j]
        else:  # 부모노드가 두개인 경우에는 둘 중에 큰 값에 현재 노드의 값을 더해준다.
            memo[i][j] = max(memo[i - 1][j], memo[i - 1][j - 1]) + arr[i][j]
print(max(memo[n - 1]))
