# 딱지놀이
N = int(input())

for _ in range(N):
    card_a = list(map(int, input().split()))
    card_b = list(map(int, input().split()))
    cnt_a = [0] * 5
    cnt_b = [0] * 5
    # 도형별로 개수 세기
    for i in range(1, card_a[0] + 1):
        cnt_a[card_a[i]] += 1
    for j in range(1, card_b[0] + 1):
        cnt_b[card_b[j]] += 1
    # 누가 이겼는지 계산
    for k in range(4, 0, -1):
        if cnt_a[k] > cnt_b[k]:
            result = 'A'
            break
        elif cnt_a[k] < cnt_b[k]:
            result = 'B'
            break
    else:
        result = 'D'
    print(result)







