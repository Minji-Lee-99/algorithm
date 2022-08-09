# 암호 생성기

from collections import deque

rule = [1, 2, 3, 4, 5]
for i in range(1, 11):
  test_case = int(input())
  pw = deque(map(int, input().split()))
  index = 0
  while 1:
    num = pw.popleft()
    num -= rule[index]
    if num <= 0:
      pw.append(0)
      break
    else:
      pw.append(num)
      index = (index + 1) % 5
  print(f'#{test_case}', end=' ')
  for i in range(len(pw)):
    print(pw.popleft(), end=' ')
  print('\n', end='')