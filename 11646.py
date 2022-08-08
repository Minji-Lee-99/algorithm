# 중력

T = int(input())
for test_case in range(1, T + 1):
  N = int(input())
  height = list(map(int, input().split()))
  max_dt = 0
  for i in range(N):
    dt = 0
    for j in range(i+1, N):
      if height[i] > height[j]:
        dt += 1
    if max_dt < dt:
      max_dt = dt
  print(f'#{test_case} {max_dt}')
