N,M = map(int,input().split())
S=[]
for _ in range(N):
    s=list(map(str,input()))
    S.append(s)
ans=0
for i in range(N-1):
    I=S[i]
    for j in range(i+1,N):
        J=S[j]
        judge=True
        for k in range(M):
            if S[i][k]!='o' and S[j][k]!='o':
                judge=False
        if judge:
            ans+=1

print(ans)


