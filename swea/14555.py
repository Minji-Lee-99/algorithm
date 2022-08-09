# 공과 잡초

T = int(input())
for test_case in range(1, T + 1):
    grassland = input()
    count = 0
    for idx in range(len(grassland)):
        if grassland[idx] == '(':
            count += 1
        elif grassland[idx] == ')' and grassland[idx - 1] != '(':
            count += 1
    print(f'#{test_case} {count}')