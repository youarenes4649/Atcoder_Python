N,K=map(int,input().split())

S=[]
set_s=set()
for i in range(N):
    s=input()
    S.append(s)
    for n in s:
        set_s.add(n)



ans=0

for i in range(1<<N):
    
    use=[]
    tmpans=0
    for j in range(N):
        if (i>>j)&1==1:
            use.append(S[j])

    if len(use)==0:
        continue

    for n in set_s:
        cnt=0
        for s in use:
            if n in s:
                cnt+=1


        if cnt==K:
            tmpans+=1

    ans=max(ans,tmpans)


print(ans)


    



