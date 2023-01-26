N=int(input())
from collections import defaultdict
name=defaultdict()
S=[]
T=[]
for i in range(N):
    s,t=input().split()

    S.append(s)
    T.append(t)

judge_s=[True]*N
judge_t=[True]*N
for i in range(N):
    for j in range(N):
        if i==j:
            continue

        s,t=S[i],T[i]

        if s ==S[j] or s==T[j]:
            judge_s[i]=False

        if t==S[j] or t==T[j]:
            judge_t[i]=False


for i in range(N):
    if judge_s[i]==False and judge_t[i]==False:
        print('No')

        exit()



print('Yes')




            



    




    


    

    

    
    

    




    


