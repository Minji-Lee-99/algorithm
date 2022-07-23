# 스도쿠 검증

# 방법 1
# [[1, 2, 3, 4, 5, 6, 7, 8, 9], [...], [...]] 이런 형태의 리스트로 입력을 받아서 검증할 때, 해당 element들을 찾아서 검증
def test_sudocu(sudocu):
    result = 1
    # 3 X 3 검증
    for k in range(3):
        for l in range(3):
            test = sudocu[k * 3][l * 3 : l * 3 + 3] + sudocu[k * 3 + 1][l * 3 : l * 3 + 3] + sudocu[k * 3 + 2][l * 3 : l * 3 + 3]
            if len(set(test)) != 9:
                result = 0
                return result
    for j in range(9):
        # 가로줄 검증
        if len(set(sudocu[j])) != 9:
            result = 0
            return result
        # 세로줄 검증
        test = []
        for i in range(9):
            test.append(sudocu[i][j])
        if len(set(test)) != 9:
            result = 0
            return result
    return result 


# 다른 사람의 코드를 보고 변형해본 코드
# 아예 입력받을 때부터 3 X 3, 가로줄, 세로줄 검증에 필요한 형태로 만드는 방법
# 왜인지 모르지만 위의 코드보다 더 느려짐
T = int(input())
for test_case in range(1, T + 1):
    sudocu = []
    for i in range(9):
        sudocu.append(list(map(int, input().split())))
    result = test_sudocu(sudocu)
    print(f'#{test_case} {result}')

def test_sudocu(lst):
    return 0 if len(set(lst)) != 9 else 1

T = int(input())
for test_case in range(1, T + 1):
    row = []
    column = [[] for i in range(9)]
    box = [[] for i in range(9)]
    for i in range(9):
        row.append(list(map(int, input().split()))) # 가로줄
        for j in range(9):
            column[j].append(row[i][j]) # 세로줄
            box[(i // 3) * 3 + (j // 3)].append(row[i][j]) # 박스
    result = 1
    for k in range(9):
        if test_sudocu(row[k]) and test_sudocu(column[k]) and test_sudocu(box[k]): #스도쿠 판단
            continue
        else:
            result = 0
    print(f'#{test_case} {result}')