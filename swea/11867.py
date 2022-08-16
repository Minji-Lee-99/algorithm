import sys
sys.stdin = open("input_11867.txt", "r")

def find_palin(words):
    for i in range(N):  # 가로 회문 찾기
        for j in range(N - M + 1):
            flag = True
            for k in range(M // 2):
                if words[i][j + k] != words[i][j + M - 1 - k]:
                    flag = False
            if flag:
                return words[i][j:j + M]
    for i in range(N):  # 세로 회문 찾기
        for j in range(N - M + 1):
            flag = True
            for k in range(M // 2):
                if words[j + k][i] != words[j + M - 1 - k][i]:
                    flag = False
            if flag:
                result = ''
                for l in range(M):
                    result += words[j + l][i]
                return result


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    words = [input() for _ in range(N)]
    print(f'#{tc} {find_palin(words)}')
