#파스칼의 삼각형

T = int(input())
for test_case in range(1, T + 1):
    num = int(input())
    print(f'#{test_case}')
    for i in range(1, num+1):
        if i <= 2: # 1~2번째줄
            print("1 " * i)
        else: # 3이상 
            print("1", end=' ')
            for j in range(i - 2):
                print(i - 1, end=' ')
            print("1", end=' ')
            print("\n", end='')