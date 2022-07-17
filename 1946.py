#간단한 압축풀기

T = int(input())
for test_case in range(1, T + 1):
    print("#%d" %test_case)
    count = int(input())
    word = [0 for i in range(count)]
    num = [0 for i in range(count)]
    total = 0
    #입력된 값들을 리스트에 저장
    for i in range(count):
        word[i], num[i] = input().split()
    #입력된 값의 압축을 푸는 과정
    for j in range(count):
        for k in range(int(num[j])):
            print(word[j], end="")
            total+=1
            #한 문자씩 출력하다가 출력한 문자의 개수가 10개면 개행하고 total 초기화
            if total==10:
                print("\n", end="")
                total=0
    print("\n", end="")





