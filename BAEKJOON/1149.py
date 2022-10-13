# RGB거리
# red[i]는 i번째 집을 빨간색으로 칠했을 때 최댓값
# (그러면 i - 1이 파란색, 초록색으로 칠한 값에 i번째 집을 빨간 색으로 칠한 값 중에 큰 값이 i번째 집을 빨간색으로 칠했을 때 최댓값이 된다.
def f(n):
    for i in range(1, n):
        red[i] = min(green[i - 1] + arr[i][0], blue[i - 1] + arr[i][0])
        green[i] = min(red[i - 1] + arr[i][1], blue[i - 1] + arr[i][1])
        blue[i] = min(red[i - 1] + arr[i][2], green[i - 1] + arr[i][2])
    return min(red[n - 1], green[n - 1], blue[n - 1])  # 결과는 N번째 집을 빨간색으로 칠한 경우, 초록색으로 칠한 경우, 파란색으로 칠한 경우 중 최댓값이 결과


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
red = [0] * n
green = [0] * n
blue = [0] * n
red[0] = arr[0][0]
green[0] = arr[0][1]
blue[0] = arr[0][2]
print(f(n))
