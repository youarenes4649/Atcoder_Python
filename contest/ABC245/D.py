N,M=map(int,input().split())
A=list(map(int,input().split()))
C=list(map(int,input().split()))

A.reverse()
C.reverse()
B=[]

for j in range(M+1):
    for i in range(1,N+1):
        a=C[j]//A[0]
        
        C[j+i]-=a*A[i]

    B.append(a)

B.reverse()
print(*B)

