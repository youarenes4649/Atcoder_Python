N,W=map(int,input().split())
A=list(map(int,input().split()))
cnt=0
count=[False]*(W+1)

for i in range(N):
    if A[i]<=W and count[A[i]]==False:
        count[A[i]]=True
        cnt+=1



for i in range(N-1):
    a=A[i]
    for j in range(i+1,N):
        if a+A[j]<=W and count[a+A[j]]==False:
            count[a+A[j]]=True

            cnt+=1

for i in range(N-2):
    a=A[i]
    for j in range(i+1,N-1):
        b=A[j]

        for k in range(j+1,N):
            if a+b+A[k]<=W and count[a+b+A[k]]==False:
                count[a+b+A[k]]=True

                cnt+=1


print(cnt)


        

