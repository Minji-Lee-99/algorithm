# 달란트

T = int(input())
for tc in range(1, T + 1):
    N, P = map(int, input().split())
    rem = N % P
    quo = N // P
    print(f'#{tc} {quo ** (P - rem) * (quo + 1) ** rem}')
