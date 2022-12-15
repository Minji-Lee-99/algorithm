# 가장 긴 증가하는 부분수열 2
N = int(input())
arr = list(map(int, input().split()))
lis = [arr[0]]
for i in range(1, N):
    if arr[i] > lis[-1]:
        lis.append(arr[i])
    else:
        result = 0
        s = 0
        e = len(lis) - 1
        while s <= e:
            mid = (s + e) // 2
            if arr[i] == lis[mid]:
                result = mid
                break
            elif arr[i] > lis[mid]:
                s = mid + 1
            else:
                e = mid - 1
                result = mid
        lis[result] = arr[i]
print(len(lis))


# from bisect import bisect_left
#
# N = int(input())
# arr = list(map(int, input().split()))
# lis = [arr[0]]
# for i in range(1, N):
#     if arr[i] > lis[-1]:
#         lis.append(arr[i])
#     else:
#         lis[bisect_left(lis, arr[i])] = arr[i]
# print(len(lis))
