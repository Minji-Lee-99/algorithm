N = int(input())
arr = list(map(int, input().split()))

s = 0
e = N - 1
answer = 2000000001
ans_list = [0, 0]
while s != e:  # 두 포인터가 가리키는 값이 같아지면 더 이상 볼 필요가 없기 때문에 멈추기
    total = arr[s] + arr[e]  # 두개의 포인터가 가리키는 값을 합하기
    if total == 0:  # 만약 두개의 합의 0이라면 더 볼 필요가 없기 때문에 멈추기
        answer = 0
        ans_list = [arr[s], arr[e]]
        break
    if abs(answer) > abs(total):  # 계산한 값이 현재 정답보다 0에 근접하다면 갱신
        answer = total
        ans_list = [arr[s], arr[e]]
    if total < 0:  # 만약 합한 값이 0보다 작다면 값을 더 키워야 하므로 s를 1 키워주기
        s += 1
    else:  # 만약 합한 값이 0보다 크다면 값을 더 작게 해야 하므로 e를 1 줄이기
        e -= 1
print(*ans_list)
