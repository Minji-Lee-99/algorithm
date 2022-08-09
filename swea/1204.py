# 최빈수 구하기
T = int(input())
for test_case in range(1, T + 1):
    case_num =int(input())
    num_dict = {}
    num_lst = list(map(int, input().split()))
    most = [0, 0]
    for i in num_lst:
        #숫자가 몇번 나왔는지 세는 과정
        if i in num_dict:
            num_dict[i] += 1
        else:
            num_dict[i] = 1
        #현재 가장 많이 나온 수를 저장하는 과정
        if num_dict[i] > most[1]:
            most[0] = i
            most[1] = num_dict[i]
        elif num_dict[i] == most[1]:#빈수가 똑같다면 더 큰수로 바꿔주기
            if i > most[0]:
                most[0] = i
    print(f'#{test_case} {most[0]}')

