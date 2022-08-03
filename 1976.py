# 시각 덧셈

T = int(input())
for test_case in range(1, T + 1):
  h1, m1, h2, m2 = map(int, input().split())
  total_h = h1 + h2 + (m1 + m2) // 60
  print(f'#{test_case} {total_h if total_h <= 12 else total_h % 13 + 1} {(m1 + m2) % 60}')
  