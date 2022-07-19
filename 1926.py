# 간단한 369게임
num = int(input())
for i in range(1, num+1):
    Snum = str(i) # 숫자를 문자 리스트로 만들어서 판단
    Snum = list(Snum)
    count = 0
    for j in Snum: # 3, 6, 9 몇개가 있는 확인
        if j in ['3', '6', '9']:
            count += 1
    if count > 0: # 3, 6, 9가 있는 경우 개수에 맞춰서 - 출력
        print('-' * count, end=' ')
    else: # 아닌 경우 숫자 그대로 출력
        print(''.join(Snum), end=' ')
