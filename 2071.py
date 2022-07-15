T = int(input())
for test_case in range(1, T + 1):
  num_lst = list(map(int, input().split()))
  total = 0
  for i in range(len(num_lst)):
    total += num_lst[i]
  print("#%d %d" %(test_case, round(total/len(num_lst))))
  