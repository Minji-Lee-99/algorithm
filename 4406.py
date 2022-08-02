# 모음이 보이지 않는 사람

T = int(input())
for test_case in range(1, T + 1):
    word = input()
    result = ''
    for char in word:
        if char not in 'aeiou':
            result += char
    print(f'#{test_case} {result}')
