N = int(input())
A = list(map(int, input().split()))
D = int(input())
L_max = [0] * (N+1)
R_max = [0] * (N+1)
for i in range(1, N+1):
    L_max[i] = max(L_max[i-1], A[i-1])
    R_max[i] = max(R_max[i-1], A[N-i])
R_max.reverse()

for _ in range(D):
    L, R = map(int, input().split())
    print(max(L_max[L-1], R_max[R]))