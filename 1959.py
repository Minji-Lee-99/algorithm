# 두개의 숫자열

# 길이가 다른 두 리스트가 주어졌을 때, 두 리스트의 곱의 합의 최댓값을 구하는 함수
def find_max_total(N, M, A, B):
    max_total = 0
    #A, B리스트의 길이 차이 + 1만큼 반복(가능한 모든 경우의 수를 판단)
    for i in range(M - N + 1):
        total = 0
        for j in range(len(A)):
            total += (A[j] * B[i + j]) 
        if max_total < total:
            max_total = total
    return max_total

T = int(input())
for test_case in range(1, T + 1):
    # 입력받는 부분
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # A리스트가 더 긴 경우, B리스트가 더 긴 경우를 나눠서 함수 호출
    result = find_max_total(N, M, A, B) if N < M else find_max_total(M, N, B, A)
    print(f'#{test_case} {result}')

