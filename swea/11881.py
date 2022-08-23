# 토너먼트 카드게임

def card(s, e):
    if e-s >= 1:
        mid = (s + e) // 2
        p1 = card(s, mid)
        p2 = card(mid + 1, e)
        if (arr[p2] == 1 and arr[p1] == 3) or (arr[p2] == 2 and arr[p1] == 1) or (arr[p2] == 3 and arr[p1] == 2):
            return p2
        else:
            return p1
    else:
        return s


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{tc} {card(0, N - 1) + 1}')
