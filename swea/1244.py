# 최대 상금

# DFS를 통해서 모든 경우를 확인하는데, 메모이제이션을 통해서 이미 나온 경우는 계산하지 않도록 함.
def find_max_price(number, k, memo):
    if k == 0: # base케이스
        return number
    if (number, k) in memo: # 메모에 있는 경우 메모값 리턴
        return memo[(number, k)]
    for i in range(len(number)): # 모든 경우의 수
        for j in range(len(number)):
            if i != j: # i, j가 같지 않을때만 실행
                number2 = list(number)
                number2[i], number2[j] = number2[j], number2[i] # 자리 바꾸기
                num = find_max_price(''.join(number2), k-1, memo) # 자리 바꾼 상태에서 다시 자리바꾸기(k번 만큼)
                if (number, k) in memo: # 메모에 적어주기
                    if memo[(number, k)] < num: # 이미 메모에 있다면 새로운 값이 더 큰 경우만 바꾸기
                        memo[(number, k)] = num
                else:
                    memo[(number, k)] = num
    return memo[(number, k)] # 메모에서 최종값 리턴


T = int(input())
for tc in range(1, T + 1):
    num, k = input().split()
    k = int(k)
    result = find_max_price(num, k, {})
    print(f'#{tc} {result}')
