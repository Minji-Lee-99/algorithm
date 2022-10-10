# RGB거리
def f(n):
    for i in range(1, n):
        red[i] = min(green[i - 1] + arr[i][0], blue[i - 1] + arr[i][0])
        green[i] = min(red[i - 1] + arr[i][1], blue[i - 1] + arr[i][1])
        blue[i] = min(red[i - 1] + arr[i][2], green[i - 1] + arr[i][2])
    return min(red[n - 1], green[n - 1], blue[n - 1])


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
red = [0] * n
green = [0] * n
blue = [0] * n
red[0] = arr[0][0]
green[0] = arr[0][1]
blue[0] = arr[0][2]
print(f(n))
