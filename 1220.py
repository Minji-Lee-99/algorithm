# Magnetic

# 1은 N 2는 S, 윗부분 N극, 아랫부분 S극
T = 10
for test_case in range(1, T + 1):
  N = int(input())
  tb=[]
  for i in range(N):
    tb.append(list(map(int, input().split())))
  count = 0
  for k in range(N):
    before = 0
    for l in range(N):
      if tb[l][k] == 1:
        before = 1
      elif tb[l][k] == 2 and before:
        count += 1
        before = 0
  print(f'#{test_case} {count}')




