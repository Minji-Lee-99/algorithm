def find_pattern(str2, str1):
    for i in range(len(str2) - len(str1) + 1):
        flag = True
        for j in range(len(str1)):
            if str2[i + j] != str1[j]:
                flag = False
                break
        if flag:
            return 1
    return 0


T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    print(f'#{tc} {find_pattern(str2, str1)}')


