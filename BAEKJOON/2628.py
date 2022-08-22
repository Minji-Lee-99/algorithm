# 종이자르기
# 자를 위치를 정렬하기 위해서 카운팅 소트 사용

w, h = map(int, input().split())
N = int(input())
w_lst = [0] * (w + 1)    # 자를 위치를 정렬하기 위한 리스트
h_lst = [0] * (h + 1)

# 자를 위치 표시
for _ in range(N):
    n1, n2 = map(int, input().split())
    if n1:
        w_lst[n2] = 1
    else:
        h_lst[n2] = 1

# 종이의 길이를 구하기 위해서 첫부분과 끝부분을 1로 변경
w_lst[0] = w_lst[w] = h_lst[0] = h_lst[h] = 1

# 자른 위치만 가지고 오기
result_w = []
for i in range(w + 1):
    if w_lst[i]:
        result_w.append(i)

result_h = []
for i in range(h + 1):
    if h_lst[i]:
        result_h.append(i)

# 계산
max_w = 0
for i in range(len(result_w) - 1):
    if result_w[i + 1] - result_w[i] > max_w:
        max_w = result_w[i + 1] - result_w[i]

max_h = 0
for i in range(len(result_h) - 1):
    if result_h[i + 1] - result_h[i] > max_h:
        max_h = result_h[i + 1] - result_h[i]

# 결과 출력
print(max_w * max_h)













