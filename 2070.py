T = int(input())
for test_case in range(1, T + 1):
  num1, num2 = map(int, input().split())
  if num1 > num2:
    print(f'#{test_case} >')
  elif num1 < num2:
    print(f'#{test_case} <')
  else:
    print(f'#{test_case} =')