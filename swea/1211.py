import sys
sys.stdin = open("input_1211.txt", "r")

for test_case in range(1, 11):
    tc = input()
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]
    starts = list(filter(lambda idx: arr[0][idx] == 1, range(N)))
    result = {}
    for start in starts:
        x = start
        y = 0
        move = 0
        while y < N - 1:
            for nx in [-1, 1]:
                if 0 <= x + nx <= N - 1 and arr[y][x + nx] == 1:
                    while 0 <= x + nx <= N - 1 and arr[y][x + nx] == 1:
                        x = x + nx
                        move += 1
                    break
            y += 1
            move += 1
        result[start] = move
    min_key = starts[0]
    for key in result:
        if result[key] < result[min_key]:
            min_key = key
    print(f'#{test_case} {min_key}')