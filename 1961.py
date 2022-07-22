# 숫자 배열 회전

T = int(input())
for test_case in range(1, T + 1):
    #데이터 입력받기
    N = int(input())
    numbers = []
    total_list = []
    for i in range(N):
        numbers.append(list(map(int, input().split())))
    total_list.append(numbers)
    # 배열 회전
    for j in range(3): # 90도씩 3번 반복
        number_box = []
        for k in range(N): # 열 고정
            temp = []
            for l in range(N-1, -1, -1): # 행을 역순으로 참조
                temp.append(total_list[-1][l][k])
            number_box.append(temp) # 각 행을 추가
        total_list.append(number_box) # 90도 회전을 완료한 이중리스트를 결과 리스트에 추가
    
    #형식에 맞게 출력
    print(f'#{test_case}')
    for i in range(N):
        for j in range(1, 3+1):
            for k in range(N):
                print(total_list[j][i][k], end = '')
            print(' ', end='')
        print('\n', end='')