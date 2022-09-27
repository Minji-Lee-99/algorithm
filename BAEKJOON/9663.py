# N-Queen
def nqueen(n, k):
    global ans
    if n == k:
        ans += 1
        return
    else:
        for i in range(N):
            for j in range(k):
                if abs(k - j) == abs(i - col[j]) or col[j] == i:
                    break
            else:
                col[k] = i
                nqueen(n, k + 1)


N = int(input())
col = [0] * N
ans = 0
nqueen(N, 0)
print(ans)
