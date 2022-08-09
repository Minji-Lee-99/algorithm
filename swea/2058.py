#자릿수더하기
#10으로 자릿수 만큼 나누어 나머지를 더하여 자릿수의 합을 구함

num = int(input())
total = 0
while num > 0:
    rem = num % 10
    num = num // 10
    total += rem
print(total)