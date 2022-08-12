# GNS

import sys
sys.stdin = open("input_1221.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    tc, N = input().split()
    N = int(N)
    text = input().split()
    cnt = {}
    order = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    result = ''
    # 개수 세기
    for num in order:
        cnt[num] = 0
    for word in text:
        cnt[word] += 1
    # 개수 만큼 출력
    for num in order:
        result += (num + ' ') * cnt[num]
    print(f'{tc} {result}')


