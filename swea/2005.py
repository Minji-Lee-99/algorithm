#파스칼의 삼각형
T = int(input())
for test_case in range(1, T + 1):
    num = int(input())
    print(f'#{test_case}')
    lst0 = []
    lst = [1]
    for i in range(num):
        print(' '.join(list(map(str, lst))))
        lst0 = [0] + lst + [0]
        lst = [(lst0[j] + lst0[j+1]) for j in range(len(lst0)-1)]
