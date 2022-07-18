#서랍의 비밀번호
#비밀번호 P, 확인해볼 번호 T가 주어질 때 몇번 확인해보아야 하는가?(ex. 123 100 -> 24)
P, T = map(int, input().split())
print(P-T+1)