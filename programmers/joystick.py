def solution(name):
    answer = 0
    StrToNum = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
                'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19,
                'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
    for i in range(len(name)):
        num = StrToNum[name[i]]
        if num == 1:
            continue
        elif num <= 13:
            answer += (num - 1)
        else:
            answer += (26-num+1)




print(solution("JEROEN"))
print(solution("JAN"))
print(solution("AAAAABBAAAAAAABAAA"))
print(solution("ABABAAAAABA"))

# length = len(name)
# count1 = 0
# count2 = 0
# if name[1] == 'A':
#     idx = 2
#     count1 += 1
#     while idx < length and name[idx] == 'A':
#         count1 += 1
#         idx += 1
# elif name[-1] == 'A':
#     idx = -2
#     count2 += 1
#     while idx >= length * -1 and name[idx] == 'A':
#         count2 += 1
#         idx -= 1
#
# if count1 >= count2:
#     answer += (length - 1 - count1)
# else:
#     answer += (length - 1 - count2)
# return answer