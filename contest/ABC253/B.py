H,W=map(int,input().split())
S=[]
for i in range(H):
    s=list(map(str,input()))
    S.append(s)

koma=[]

for i in range(H):
    for j in range(W):
        if S[i][j]=='o':
            koma.append((i,j))

xs,ys=koma[0]
xg,yg=koma[1]
ans=abs(xs-xg)+abs(ys-yg)
print(ans)

