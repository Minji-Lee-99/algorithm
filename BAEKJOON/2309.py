# 일곱 난쟁이

height = []
rem = 0

# 아홉 난쟁이 키 입력받기
for _ in range(9):
    height.append(int(input()))
height.sort()

# 100보다 얼마가 초과되는지 계산
for h in height:
    rem += h
rem -= 100

# 두 난쟁이의 키의 합이 초과와 같아지는 경우 찾기
for i in range(9):
    for j in range(i + 1, 9):
        if height[i] + height[j] == rem:
            result = [i, j]
            break

# 결과 출력
for i in range(9):
    if i not in result:
        print(height[i])
