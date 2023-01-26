N,K=map(int,input().split())
A=list(map(int,input().split()))
X,Y=[],[]
X_A,Y_A=[],[]
for i in range(N):
        xn,yn=map(int,input().split())
        X.append(xn)
        Y.append(yn)
for a in A:
    a-=1
    X_A.append(X[a])
    Y_A.append(Y[a])



dist_max=0
for i in range(len(X)):
    dist=10**20

    xn,yn=X[i],Y[i]
    for a in range(len(X_A)):
        xa,ya=X_A[a],Y_A[a]
        dis=((xn-xa)**2+(yn-ya)**2)**0.5
        dist=min(dist,dis)

    dist_max=max(dist_max,dist)


print(dist_max)

        

        