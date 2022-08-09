#중간값찾기

T = int(input())
num_list = list(map(int, input().split()))

#버블 소트
for i in range(T):
    for j in range(T-(i+1)):
        if num_list[j] > num_list[j+1]:
            num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

#중간값 출력
print(num_list[T//2])
