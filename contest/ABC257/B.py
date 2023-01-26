N,K,Q=map(int,input().split())
A=list(map(int,input().split()))
L=list(map(int,input().split()))

for q in L:
    q-=1#idxを合わせる
    if q==K-1:
        if A[q]!=N:
            A[q]+=1

    else:
        if A[q]+1 !=A[q+1]:
            A[q]+=1

print(*A)