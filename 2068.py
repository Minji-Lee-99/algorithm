T = int(input())
for test_case in range(1, T + 1):
  num_lst = list(map(int, input().split()))
  max_num = num_lst[0]
  for i in range(0, len(num_lst)):
    if max_num < num_lst[i]:
      max_num = num_lst[i]
      