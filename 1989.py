#초심자의 회문 검사

#회문인지 검사하는 재귀함수
def palin(word):
    #단어의 길이가 1이거나 0이면 판단할 필요가 없으므로 true
    if len(word) <= 1:
        return True
    #첫번째 문자와 마지막 문자가 같다면, 두번째 문자와 끝에서 두번째 문자를 재귀를 통해 판별
    elif word[0] == word[-1]:
        return palin(word[1:-1])
    #위의 두 경우가 아니면 회문이 아니기에 FALSE
    else:
        return False

T = int(input())
for test_case in range(1, T + 1):
    print("#%d %d" %(test_case, int(palin(input()))))
