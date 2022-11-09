# 그래프
from collections import deque

def solution(n, edge):
    answer = 0
    visited = [-1] * (n + 1)
    adj = [[] for _ in range(n + 1)]
    for x, y in edge:  # 리스트 형식으로 간선 바꿔주기
        adj[x].append(y)
        adj[y].append(x)
    q = deque([1])
    visited[1] = 0
    while q:  # q가 비었을 때까지 실행
        s = q.popleft()
        for v in adj[s]:
            if visited[v] == -1 or visited[v] > visited[s] + 1:  # 아직 갱신이 안되었거나, 더 빠른 길이 있다면 갱신
                visited[v] = visited[s] + 1
                q.append(v)  # 갱신되면 q에 넣어주어야 함
    max_v = 0  # 가장 큰 값 저장
    max_cnt = 0  # 가장 큰 값의 개수
    for d in visited:
        if d > max_v:  # d가 max_v보다 크다면 max_cnt, max_v를 모두 초기화
            max_cnt = 1
            max_v = d
        elif d == max_v:  # d == max_v이면 개수 카운트
            max_cnt += 1
    answer = max_cnt
    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))