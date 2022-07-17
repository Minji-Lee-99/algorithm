#홀수만 더하기
#22.04.27
T = int(input())
for test_case in range(1, T + 1):
    num = list(map(int, input().split()))
    total=0
    for i in range(len(num)):
        if num[i]%2 ==1:
            total+=num[i]
    print('#%d %d' %(test_case, total))