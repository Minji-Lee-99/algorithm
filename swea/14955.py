# 전기버스

T = int(input())
for test_case in range(1, T + 1):
    k, n, m = map(int, input().split())
    m_lst = list(map(int, input().split()))
    now = cnt = 0 # 현재 위치를 저장하는 변수와 충전 횟수를 저장하는 변수
    idx = -1 # m_lst탐색 위치를 저장하는 변수
    while now + k < n: # 현재 위치에서 목표지점까지 갈 수 있다면 반복문 종료
        flag = False
        for i in range(idx + 1, m): # 현재 위치에서 갈 수 있는 충전소 탐색
            if m_lst[i] <= now + k:
                idx = i
                flag = True
            else:
                break
        if flag: # 있다면 현재 위치 및 충전 횟수 갱신
            now = m_lst[idx]
            cnt += 1
        else: # 없다면 끝까지 도달할 수 없기 때문에 반복문 종료
            cnt = 0
            break
    print(f'#{test_case} {cnt}')



# T = int(input())
# for test_case in range(1, T + 1):
#     k, n, m = map(int, input().split())
#     m_lst = list(map(int, input().split()))
#     now_k = k
#     cnt = 0
#     for i in range(1, n + 1): # 각 정류장을 하나하나 방문
#         now_k -= 1 # 갈 수 있는 거리 감소
#         if now_k < 0: # 더 이상 갈 수 있는 거리가 없는 경우
#             cnt = 0
#             break
#         if i + now_k >= n: # 현재 위치에서 목표점까지 도달할 수 있는 경우
#             break
#         if i in m_lst: # 현재 위치에 충전소가 있는 경우
#             if now_k == 0: # 더이상 갈 수 있는 거리가 없다면 충전
#                 now_k = k
#                 cnt += 1
#             else:
#                 flag = False
#                 for j in m_lst: # 갈 수 있는 거리 중 충전할 수 있는 곳이 있는지 확인
#                     if i < j <= i + now_k:
#                         flag = True
#                         break
#                 if not flag: # 더 앞에 충전할 곳이 없다면 충전
#                     now_k = k
#                     cnt += 1
#     print(f'#{test_case} {cnt}')





