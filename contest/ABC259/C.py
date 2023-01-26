#ランレングス圧縮
S=input()
T=input()
if S==T:
    print('Yes')
    exit()
s_ls=[]
t_ls=[]
for s in S:
    if len(s_ls)==0:
        s_ls.append([s,1])

    else:
        if s_ls[-1][0]==s:
            s_ls[-1][1]+=1

        else:
            s_ls.append([s,1])
for t in T:
    if len(t_ls)==0:
        t_ls.append([t,1])

    else:
        if t_ls[-1][0]==t:
            t_ls[-1][1]+=1

        else:
            t_ls.append([t,1])

if len(s_ls)!=len(t_ls):
    print('No')
    exit()

else:
    for i in range(len(s_ls)):
        s,ns=s_ls[i]
        t,nt=t_ls[i]
        if s!=t:
            print('No')
            exit()
        if ns==1 and nt>1:
            print('No')
            exit()
        if ns>nt:
            print('No')
            exit()

        
print('Yes')

