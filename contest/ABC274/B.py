H,W=map(int,input().split())
C=[]
for i in range(H):
    c=list(input())
    C.append(c)

X=[]
for j in range(W):
    xj=0
    for i in range(H):
        if C[i][j]=='#':
            xj+=1

    X.append(xj)

print(*X)
        
