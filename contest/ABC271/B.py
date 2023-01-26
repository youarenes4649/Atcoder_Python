N,Q=map(int,input().split())
L=[]
A=[]
for i in range(N):
    all=list(map(int,input().split()))
    l=all[0]
    a=all[1:]
    L.append(l)
    A.append(a)

for q in range(Q):
    s,t=map(int,input().split())
    s-=1
    t-=1
    print(A[s][t])