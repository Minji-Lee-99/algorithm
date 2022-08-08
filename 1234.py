# 비밀번호

for test_case in range(1, 11):
  N, pw = input().split()
  N = int(N)
  pw = list(pw)
  i = 0
  while i < N - 1:
    if pw[i] == pw[i + 1]:
      pw = pw[:i] + pw[i+2:]
      i -= 1
      N -= 2
      continue
    i += 1
  print(f'#{test_case} {"".join(pw)}')