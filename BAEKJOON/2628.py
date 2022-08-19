w, h = map(int, input().split())
N = int(input())
w_lst = [0] * (w + 1)
h_lst = [0] * (h + 1)
for _ in range(N):
    n = int(input())
    if n[0]:
        w_lst[n[1]] = 1
    else:
        h_lst[n[1]] = 1
w_lst[0] = w_lst[w] = h_lst[0] = h_lst[h] = 1













