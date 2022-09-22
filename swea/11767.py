# 11767 탐욕 알고리즘 베이비진 게임
def check(count):
    t = r = 0
    i = 0
    while i < 10:
        if count[i] >= 3:
            t += 1
            count[i] -= 3
            continue
        if count[i] > 0 and count[i + 1] > 0 and count[i + 2] > 0:
            r += 1
            count[i] -= 1
            count[i + 1] -= 1
            count[i + 2] -= 1
            continue
        i += 1
    return t + r


def babygin(num):
    count = [0] * 12
    # 먼저 3장 넣기
    for i in range(3):
        count[num[i]] += 1
    if check(count):
        return i
    # 그 다음 한장씩 넣으면서 tri, run나왔는지 확인
    for i in range(3, 6):
        count[num[i]] += 1
        if check(count):
            return i
    return 10


T = int(input())
for tc in range(1, T + 1):
    num = list(map(int, input().split()))
    p1 = babygin(num[0:12:2])
    p2 = babygin(num[1:12:2])
    # 더 빨리 나온 쪽이 승리
    if p1 < p2:
        ans = 1
    elif p1 > p2:
        ans = 2
    elif p1 == p2 and p1 != 10:
        ans = 1
    else:
        ans = 0
    print(f'#{tc} {ans}')
