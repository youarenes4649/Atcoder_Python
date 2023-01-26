N=int(input())
P=list(map(int,input().split()))
ancester=[-1]*(N+1)

for i,x in enumerate(P):
    
    ancester[i+2]=x
cnt=0
x=N
while x!=1:
    x=ancester[x]
    cnt+=1

print(cnt)

