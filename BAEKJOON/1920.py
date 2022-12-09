# 수 찾기
# 간단한 binary search문제

def binary_search(target):
    s = 0
    e = N - 1
    while s <= e:  # s와 e가 역전되면, 내가 찾는 숫자가 없는 것
        mid = (s + e) // 2
        if A[mid] == target:
            return 1
        elif A[mid] > target:
            e = mid - 1
        else:
            s = mid + 1
    return 0


N = int(input())
A = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))
A.sort()  # binary search는 항상 정렬되어 있어야 함
for t in targets:
    print(binary_search(t))

