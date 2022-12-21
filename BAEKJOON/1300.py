# k번째 수
def find_under(n):  # i * j를 했을 때, n보다 작은 수가 몇개 있는지 확인하는 함수
    cnt = 0
    for i in range(1, N + 1):
        cnt += min(n // i, N)  # i와 j는 N보다 작거나 같기 때문에 n // i값이 N보다 크면 N개!
    return cnt


N = int(input())
K = int(input())
s = 1  # 시작점
e = N ** 2  # 끝점
answer = N ** 2
while s <= e:  # s가 e를 역전하면 멈추기
    mid = (s + e) // 2
    cnt = find_under(mid)
    if cnt < K:  # mid보다 작거나 같은 수의 개수가 목표 K보다 작으면 s를 갱신
        s = mid + 1
    else:  # mid보다 작거나 같은 수의 개수가 목표 k보다 크거나 같으면 answer를 mid로 갱신하고 e를 갱신해준다.
        answer = mid
        e = mid - 1
print(answer)
