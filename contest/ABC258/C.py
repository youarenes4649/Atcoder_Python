N,Q=map(int,input().split())
S=input()
len_s=len(S)
total=0
for q in range(Q):
    t,x=map(int,input().split())

    if t==1:
        total+=x

    if t==2:
        ans=total%len_s
        print(S[x-(ans+1)])