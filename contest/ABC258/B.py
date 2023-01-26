N=int(input())
A=[]
for i in range(N):
    a=list(map(str,input()))
    A.append(a)

zx=[1,-1,0,0,1,1,-1,-1]
zy=[0,0,1,-1,1,-1,1,-1]
ans=0
for x,y in zip(zx,zy):
    
    
    for i in range(N):
        for j in range(N):
            tmp=''
        
            tmp=''.join(str(A[i][j]))
            nx=i
            ny=j
            for n in range(N-1):
                nx=nx+x
                ny=ny+y
                tmp+=''.join(str(A[(nx)%N][(ny)%N]))
                
            
        
            ans=max(int(ans),int(tmp))
print(ans)


            

