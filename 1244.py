# 최대 상금

import sys
sys.stdin = open("input.txt", "r")

def dfs():


T = int(input())
for tc in range(1, T + 1):
    num, K = input().split()
    K = int(K)
    num = list(num)
