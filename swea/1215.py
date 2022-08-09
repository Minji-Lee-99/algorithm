# 회문

# word가 회문인지 확인하는 함수
def is_palin(word):
    if len(word) <= 1:
        return True
    return word[-1] == word[0] and is_palin(word[1:-1])

# list가 주어졌을 때 회문이 몇개인지 확인하는 함수
def find_palin(N, num_board):
    count = 0
    for k in range(8):
        for l in range(8 - N + 1):
            temp = []
            for a in range(N):
                temp.append(num_board[l + a][k])
            if is_palin(temp):
                count += 1
            if is_palin(num_board[k][l:l+N]):
                count += 1
    return count

#main 코드
for test_case in range(1, 11):
    N = int(input())
    num_board = []
    for i in range(8):
        num_board.append(list(input()))
    if N == 1:
        count = 64
    else:
        count = find_palin(N, num_board)
    print(f'#{test_case} {count}')