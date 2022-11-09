# 그래프
from collections import deque


def solution(n, results):
    answer = 0
    adj = [[] for _ in range(n + 1)]  # 순방향 adj i번 인덱스에 i번 사람이 이긴 사람들이 있음
    adj_reverse = [[] for _ in range(n + 1)]  # 역방향 adj i번 인덱스에 i번 사람이 진 사람들이 있음
    lose = [0] * (n + 1)  # i번이 진 사람 수
    win = [0] * (n + 1)  # i번 사람이 이긴 사람 수

    # 연결 리스트 구현하기
    for x, y in results:
        adj[x].append(y)
        adj_reverse[y].append(x)

    # i번이 이긴 사람 수 계산(adj를 i번 부터 시작해서 탐색헀을 때, 도달할 수 있는 노드의 개수가 이긴 사람의 총 수)
    for i in range(1, n + 1):
        q = deque([i])
        visited = [0] * (n + 1)
        cnt = 0
        while q:
            s = q.popleft()
            for v in adj[s]:
                if not visited[v]:
                    visited[v] = 1
                    cnt += 1
                    q.append(v)
        win[i] = cnt

    # i번이 진 사람 수 계산(adj_reverse를 i번부터 시작해서 탐색했을 때, 도달할 수 있는 노드의 개수가 진 사람의 수)
    for i in range(1, n + 1):
        q = deque([i])
        visited = [0] * (n + 1)
        cnt = 0
        while q:
            s = q.popleft()
            for v in adj_reverse[s]:
                if not visited[v]:
                    visited[v] = 1
                    cnt += 1
                    q.append(v)
        lose[i] = cnt

    # 총 개수 계산(이긴 사람의 수와 진 사람의 수를 합했을 때, 참가한 선수들의 수와 같다면 i번째 사람의 순위를 특정 가능
    for i in range(1, n + 1):
        if win[i] + lose[i] == n - 1:
            answer += 1
    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
print(solution(5, [[1, 2], [4, 5], [3, 4], [2, 3]]))