# 숫자 카드 2
# 이분탐색을 이용하지 않고, 딕셔너리를 이용해서 가지고 있는 숫자 카드의 개수를 저장해두고,
# get메서드를 이용해서 저장되어 있지 않은 경우에는 0을 출력한다.

N = int(input())
A = list(map(int, input().split()))
M = int(input())
target = list(map(int, input().split()))
cnt = {}
for num in A:
    if num in cnt:
        cnt[num] += 1
    else:
        cnt[num] = 1

for t in target:
    print(cnt.get(t, 0), end=" ")
