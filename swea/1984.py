# 중간 평균값 구하기

# 방법 1
# lst전체의 합을 구하고 max_num과 min_num을 찾아서 빼고 평균을 낸다. 
T = int(input())
for test_case in range(1, T + 1):
    num_lst = list(map(int, input().split()))
    minimum = num_lst[0]
    maximum = num_lst[0]
    total = 0
    for num in num_lst: # O(n)
        if num > maximum:
            maximum = num
        elif num < minimum:
            minimum = num
        total += num
    total = (total - maximum - minimum) / (len(num_lst) - 2)
    print(f'#{test_case} {round(total)}')

# 방법 2
# 정렬하여 제일 작은 값과 큰 값을 빼고 평균을 낸다. 
T = int(input())
for test_case in range(1, T + 1):
    num_lst = sorted(list(map(int, input().split())))
    num_lst = num_lst[1:-1]
    print(num_lst)
    print(f'#{test_case} {round(sum(num_lst) / len(num_lst))}')