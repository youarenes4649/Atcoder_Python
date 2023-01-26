N=int(input())
A=list(map(int,input().split()))
P=0
count=[0]*(N)

for i in range(N):
    a=A[i]
    for j in range(i+1):
        count[j]+=a


for i in range(N):
    if count[i]>=4:
        P+=1

print(P)

