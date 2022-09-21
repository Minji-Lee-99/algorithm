# 암호코드
import sys
sys.stdin = open("1242_input.txt", "r")

# 16진수를 2진수로 바꾸는 dict
convert = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100',
           '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001',
           'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110',
           'F': '1111'}

# 0과 1의 비율로 숫자 찾는 dict
convert_rate = {'211': 0, '221': 1, '122': 2, '411': 3, '132': 4, '231': 5,
                '114': 6, '312': 7, '213': 8, '112': 9}

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())   # row, col
    code = [input().strip() for _ in range(N)]

    # 16진수를 2진수로 변환
    for i in range(N):
        temp = ''
        for j in range(M):
            temp += convert[code[i][j]]
        code[i] = temp

    # 코드 찾기
    ans = []
    for i in range(1, N - 1):
        j = 0
        while(j < M * 4 - 1):
            if code[i][j] == '1' and code[i - 1][j] == '0':  # 1이고 바로 위의 값이 0인 경우 찾기
                rate = []
                before = '1'
                for _ in range(3):  # 비율 3자리 찾기(첫번째 0은 필요X)
                    cnt = 0
                    while 1:
                        if code[i][j] == before:
                            cnt += 1
                        else:
                            rate.append(cnt)
                            before = str(abs(int(before) - 1))
                            break
                        j += 1
                # 비율에 해당하는 10진수 찾기
                minV = min(rate)
                rate = list(map(lambda x: str(x // minV), rate))
                rate = ''.join(rate)
                if rate in convert_rate:
                    ans.append(convert_rate[rate])
            else:
                j += 1

    # 올바른 암호코드인지 판단하기
    result = 0
    for i in range(0, len(ans), 8):  # 8자리씩 끊어서 확인하기
        even_num = 0
        for j in range(i+1, i + 8, 2):
            even_num += ans[j]
        odd_num = 0
        for j in range(i, i + 8, 2):
            odd_num += ans[j]
        if (odd_num * 3 + even_num) % 10 == 0:
            result += odd_num
            result += even_num
    print(f'#{tc} {result}')



# 제일 처음에 짠 코드 비효율적!
# 제일 뒤에서 보면서 1이 나오면 8글자를 모두 찾도록 해서 한 줄에서 굉장히 많은 비교를 하게 되어 있음.
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())  # row, col
#     code = [input().strip() for _ in range(N)]
#     ans = 0
#
#     # 16진수를 2진수로 변환
#     for i in range(N):
#         temp = ''
#         for j in range(M):
#             temp += convert[code[i][j]]
#         code[i] = temp
#
#     # 끝이 1인 값 찾기
#     for i in range(1, N - 1):
#         for j in range(M * 4 - 2, 0, -1):
#             if code[i][j] == '1' and code[i - 1][j] == '0':
#                 y = j
#                 temp = []   # 8자리의 숫자를 더하는 변수
#                 for k in range(8):
#                     rate = []  # 숫자 하나의 코드 비율
#                     before = '1'
#                     cnt = 0
#                     while len(rate) < 4 and y > 0:   # y가 인덱스를 벗어나면 멈춤. 그리고 rate가 4일때까지만 진행
#                         if code[i][y] == before:    # 같은 숫자이면 개수 세주기
#                             cnt += 1
#                             y -= 1
#                         else:
#                             if cnt:
#                                 rate.append(cnt)
#                             else:
#                                 break
#                             cnt = 0
#                             before = str(abs(int(before) - 1))
#                     if k == 7:  # 마지막인 경우에는 0의 개수가 추가되지 않기 때문에 따로 추가해준다.
#                         rate.append(9)
#                     if len(rate) == 4:  # 비율의 개수가 4개인 경우
#                         rate = rate[:3]
#                         minV = min(rate)
#                         rate = list(map(lambda x: str(x // minV), rate))
#                         rate = rate[::-1]
#                         rate = ''.join(rate)
#                         if rate in convert_rate:
#                             temp.append(convert_rate[rate])
#                         else:   # 비율값이 존재X
#                             break
#                     else:    # rate의 길이가 4가 안되는 경우(y가 인덱스를 벗어난 경우)
#                         break
#                 else:    # 중간에 멈추는 것 없이 8개의 숫자를 다 찾았다면 검증
#                     even_num = 0
#                     for n in range(0, 8, 2):
#                         even_num += temp[n]
#                     odd_num = 0
#                     for n in range(1, 8, 2):
#                         odd_num += temp[n]
#                     if (odd_num * 3 + even_num) % 10 == 0:
#                         ans += sum(temp)
#     print(f'#{tc} {ans}')


















