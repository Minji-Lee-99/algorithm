# flatten

for test_case in range(1, 11):
    N = int(input())
    nums = list(map(int, input().split()))
    max_i = min_i = 0
    for _ in range(N):
        for i in range(100):
            if nums[max_i] < nums[i]:
                max_i = i
            if nums[min_i] > nums[i]:
                min_i = i
        nums[max_i] -= 1
        nums[min_i] += 1
    for j in range(100):
        if nums[max_i] < nums[j]:
            max_i = j
        if nums[min_i] > nums[j]:
            min_i = j
    print(f'#{test_case} {nums[max_i] - nums[min_i]}')