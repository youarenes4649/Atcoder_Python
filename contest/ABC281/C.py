N,T=map(int,input().split())
A=list(map(int,input().split()))
A_sum=sum(A)
t_mod=T%A_sum
t_mod_ans=T%A_sum
for i in range(N):
    t_mod-=A[i]
    if t_mod<0:
        print(i+1,t_mod+A[i])
        exit()
    
