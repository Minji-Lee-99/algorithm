import sys
sys.stdin = open("input_1216.txt", "r")

for _ in range(10):
    tc = int(input())
    N = 100
    arr = [input() for _ in range(N)]
    max_len = 2
    for i in range(N): # 시작 좌표
        for j in range(N - 1):
            for k in range(max_len + 1, N-j+1): # 회문의 길이
                flag_w = True
                flag_h = True
                for l in range(k//2): # 가로 회문 판별
                    if arr[i][j+l] != arr[i][j+k-1-l]:
                        flag_w = False
                        break
                for l in range(k // 2): # 세로 회문 판별
                    if arr[j+l][i] != arr[j+k-1-l][i]:
                        flag_h = False
                        break
                if flag_w or flag_h:
                    if max_len < k:
                        max_len = k
    print(f'#{tc} {max_len}')