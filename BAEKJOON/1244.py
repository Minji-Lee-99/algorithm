# 스위치 켜고 끄기

N = int(input())
switch = list(map(int, input().split()))
M = int(input())
on_off = [1, 0]

for _ in range(M):
    s, num = map(int, input().split())
    if s == 1:  # 남학생
        i = num
        while i <= N:
            switch[i - 1] = on_off[switch[i - 1]]
            i += num    # num의 배수
    else:   # 여학생
        i = 1   # 입력받은 스위치에서 얼마나 멀어지는지를 저장하는 변수
        num = num - 1
        temp = [num]    # 입력받은 스위치는 미리 넣어두기
        while 0 <= num - i < N and 0 <= num + i < N and switch[num - i] == switch[num + i]:
            # num - i, num + i(대칭으로 한칸씩 멀리 이동)가 범위를 벗어나지 않고 대칭이라면 temp에 넣기
            temp.append(num - i)
            temp.append(num + i)
            i += 1  # 그 다음 부분도 대칭인지 확인하기 위해서 i갱신
        for idx in temp:
            # temp에 있는 인덱스에 있는 값들을 변경
            switch[idx] = on_off[switch[idx]]
# 출력
for i in range(N):
    print(switch[i], end=' ')
    # 20개 출력했으면 줄바꿈
    if (i + 1) % 20 == 0:
        print('\n', end='')
