# 암호 만들기
# 113112KB
# 116ms
def comb(n, k, s, v, c):
    if n == k:
        if v >= 1 and c >= 2:
            print(''.join(p))
        return
    if v < 1 and vowel[s] == 0:
        return
    if c < 2 and consonant[s] < 2 - c:
        return
    for i in range(s, N - (n - k) + 1):
        p[k] = a[i]
        if check[i] == 1:
            comb(n, k + 1, i + 1, v + 1, c)
        else:
            comb(n, k + 1, i + 1, v, c + 1)


R, N = map(int, input().split())
a = input().split()
a.sort()
vowel = [0] * (N + 1)  # 모음의 누적합 개수
consonant = [0] * (N + 1)  # 자음의 누적합 개수
check = [0] * N  # a의 i번 인덱스가 모음이면 1, 자음이면 0
for i in range(N - 1, -1, -1):
    if a[i] in 'aeiou':
        vowel[i] = vowel[i + 1] + 1
        consonant[i] = consonant[i + 1]
        check[i] = 1
    else:
        consonant[i] = consonant[i + 1] + 1
        vowel[i] = vowel[i + 1]
p = [''] * R
comb(R, 0, 0, 0, 0)
