N,K,X=map(int,input().split())
A=list(map(int,input().split()))
a_sum=sum(A)
A.sort(reverse=True)
for i in range(N):
    
    a=A[i]//X #何枚クーポン使えるか
    if K-a<0:
        A[i]-=K*X
        K=0

    if K==0:
        break

    if a>=1:
        A[i]-=X*a
        K-=a

A.sort(reverse=True)
if K>0:
    A=A[K:]


print(sum(A))






    
    
    
    



