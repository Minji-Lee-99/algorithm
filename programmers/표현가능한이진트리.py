import math


def solution(numbers):
    answer = []
    for num in numbers:
        bin_num = str(bin(num))[2:]
        length = len(bin_num)
        k = math.ceil(math.sqrt(length + 1))
        bin_num = ('0' * ((2 ** k - 1) - length)) + bin_num
        result = 1
        for i in range(1, len(bin_num), 2):
            if bin_num[i] == '0' and (bin_num[i - 1] == '1' or bin_num[i + 1] == '1'):
                result = 0
                break
        answer.append(result)
    return answer


print(solution([7, 42, 5, 58]))
print(solution([63, 111, 95]))
