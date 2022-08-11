# Ladder1

import sys
sys.stdin = open("input_1210.txt", "r")


# 목표지점(2)에 다다르는 시작점 찾기 함수
def find_goal(arr, starts):
    for start in starts:
        x = start
        y = 0
        while y < N - 1: # y가 끝에 도달하면 끝내기
            for nx in [-1, 1]: # 좌우측으로 갈 수 있는 곳 확인 및 이동
                if 0 <= x + nx <= N - 1 and arr[y][x + nx] == 1:
                    while 0 <= x + nx <= N - 1 and arr[y][x + nx] == 1:
                        x = x + nx
                    break
            y += 1 # 아래로 내려가기
            if arr[y][x] == 2: # 만약 이동한 곳이 목표라면 함수 종료
                return start


for test_case in range(1, 11):
    tc = input()
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]
    starts = filter(lambda idx: arr[0][idx] == 1, range(N))
    x = find_goal(arr, starts)
    print(f'#{test_case} {x}')

