# 백준 2470 두 용액
# 투 포인터
N = int(input())
arr = list(map(int, input().split()))
arr.sort()

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


# 내가 생각한 방법: 각 용액에서 가장 가까운 숫자들을 찾아서 합 계산하는 방법
# def lower_bound1(arr, n):  # n 이상인 숫자가 처음 시작하는 인덱스
#     s = 0
#     e = len(arr) - 1
#     idx = 0
#     while s <= e:
#         mid = (s + e) // 2
#         if arr[mid] >= n:
#             idx = mid
#             e = mid - 1
#         else:
#             s = mid + 1
#     return idx
#
#
# def lower_bound2(arr, n):  # n 이하인 숫자가 처음 시작하는 인덱스
#     s = 0
#     e = len(arr) - 1
#     idx = 0
#     while s <= e:
#         mid = (s + e) // 2
#         if arr[mid] <= n:
#             idx = mid
#             s = mid + 1
#         else:
#             e = mid - 1
#     return idx
#
#
# def solution():
#     global rs, rs_list
#     if len(basicity) == 0:  # 염기성이 하나도 없는 경우
#         rs_list = acid[0: 2]
#         return
#     if len(acid) == 0:  # 산성이 하나도 없는 경우
#         rs_list = [basicity[1] * -1, basicity[0] * -1]
#         return
#     for i in range(len(acid)):
#         idx1 = lower_bound1(basicity, acid[i])  # acid[i]보다 크거나 같은 것 중 가장 작은 값
#         idx2 = lower_bound2(basicity, acid[i])  # acid[i]보다 작거나 같은 것 중 가장 큰 값
#         if abs(acid[i] - basicity[idx1]) < rs:
#             rs = abs(acid[i] - basicity[idx1])
#             rs_list = [basicity[idx1] * -1, acid[i]]
#         if abs(acid[i] - basicity[idx2]) < rs:
#             rs = abs(acid[i] - basicity[idx2])
#             rs_list = [basicity[idx2] * -1, acid[i]]
#         if i == 0 and len(acid) > 2 and acid[0] + acid[1] < rs:  # aicd에서 두개를 더한 값이 정답인 경우
#             rs = acid[0] + acid[1]
#             rs_list = acid[0:2]
#         if i != 0 and acid[0] + acid[i] < rs:
#             rs = acid[0] + acid[i]
#             rs_list = [acid[0], acid[i]]
#         if rs == 0:  # 0인 경우가 있다면 더 이상 보지ㄷ 않아도 된다.
#             return
#     if len(basicity) > 2 and basicity[0] + basicity[1] < rs:  # 염기성끼리 더하는 경우 확인해주기
#         rs_list = [basicity[1] * -1, basicity[0] * -1]
#     return
#
#
# N = int(input())
# arr = list(map(int, input().split()))
# acid = list(filter(lambda x: x >= 0, arr))  # 값이 양수인 것들
# basicity = list(filter(lambda x: x < 0, arr))  # 값이 음수인 것들
# basicity = list(map(lambda x: x * -1, basicity))  # 절대값 비교를 위해서 -1 곱해주기
# acid.sort()
# basicity.sort()
# rs_list = []
# rs = 100000
# solution()
# print(rs_list)
