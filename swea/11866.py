T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    str1 = set(list(str1))
    result = {}
    for char in str1:
        result[char] = 0
    for char in str2:
        if char in result:
            result[char] += 1
    max_cnt = 0
    for key in result:
        if max_cnt < result[key]:
            max_cnt = result[key]
    print(f'#{tc} {max_cnt}')