N,K= map(int,input().split())
L =list(map(int,input().split()))
S = sorted(L)
Ls = [sorted(L[i::K])for i in range(min(N,K))]
NL=[Ls[i%K][i//K] for i in range(N)]

if S==NL:
    print('Yes')

else:
    print('No')

