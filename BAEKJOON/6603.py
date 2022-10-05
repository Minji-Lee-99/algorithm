# 로또(조합)
# 144ms
def comb(n, k, s):  # n==6
    if n == k:
        print(*p)
        return
    if num[0] - s < 6 - k:  # 뽑아야 하는 개수보다 뽑을 수 있는 수가 더 적은 경우
        return
    else:
        for i in range(s + 1, num[0] + 1):
            p[k] = num[i]
            comb(n, k + 1, i)


num = input()
while num != '0':
    num = list(map(int, num.split()))
    p = [0] * 6
    comb(6, 0, 0)
    print('\n', end="")
    num = input()
