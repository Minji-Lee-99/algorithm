# 달팽이 업그레이드
# 아래 초기 선언된 arr처럼 선언하고 이를 일반적인 달팽이 형식으로 정렬하여 출력하는 문제
# 셀렉션 소트 방식을 사용해서 정렬
# 먼저 바꿀 자리 선정
# 그다음 change함수를 통해서 그 이후 인덱스부터 가장 작은 값을 찾아서 자리 변경
from copy import deepcopy


def change(i, j, idx, k):
    """
    :param i, j: 시작위치
    :param idx: 현재 방향
    :param k: 현재 얼만큼 진행되었는지(몇번 반복문을 돌릴지 판단하기 위해서 필요)
    시작위치 이후부터 탐색하여 가장 작은 원소를 찾고 자리 바꾸기
    """
    min_i = x = i
    min_j = y = j
    visited2 = deepcopy(visited)    # 방문 배열 복사
    for _ in range(n ** 2 - k - 1):
        while 1:
            ni = i + di[idx]
            nj = j + dj[idx]
            if 0 <= ni < n and 0 <= nj < n and not visited2[ni][nj]:
                i = ni
                j = nj
                visited2[i][j] = True
                if arr[min_i][min_j] > arr[i][j]:
                    min_i = i
                    min_j = j
                break
            else:
                idx = (idx + 1) % 4
    arr[min_i][min_j], arr[x][y] = arr[x][y], arr[min_i][min_j]


# 배열 선언
arr = [[9, 20, 2, 18, 11],
       [19, 1, 25, 3, 21],
       [8, 24, 10, 17, 7],
       [15, 4, 16, 5, 6],
       [12, 13, 22, 23, 14]]
n = 5   # 배열의 크기
visited = [[False] * n for _ in range(n)]   # 방문 배열

di = [0, 1, 0, -1]  # 방향 벡터
dj = [1, 0, -1, 0]
idx = 0    # 방향벡터 인덱스

i = j = ni = nj = 0

# 배열의 크기만큼 반복
for k in range(n ** 2 - 1):
    while 1:
        # 만약 인덱스가 범위를 벗어나지 않았고, 방문하지 않았다면
        if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
            i = ni
            j = nj
            visited[i][j] = True    # 방문 처리
            change(i, j, idx, k)    # 가장 작은 원소를 찾아서 변경
            ni = i + di[idx]    # 다음 위치 갱신
            nj = j + dj[idx]
            break
        # 만약 인덱스가 범위를 벗어났거나, 방문했다면
        else:
            # 방향벡터 갱신 및 다음 위치 갱신
            idx = (idx + 1) % 4
            ni = i + di[idx]
            nj = j + dj[idx]

for i in range(n):
    print(arr[i])