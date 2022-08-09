# 패턴 마디의 길이
T = int(input())
for test_case in range(1, T + 1):
    sentence = input()
    for i in range(1, 11):
        word_length = i # 마디의 길이
        #첫마디와 두번째 마디의 단어가 같다면 그 길이가 마디의 길이가 된다. 
        if sentence[0 : word_length] == sentence[word_length : word_length*2]:
            break
    print(f'#{test_case} {word_length}')
