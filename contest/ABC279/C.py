#pypyはdefaultdictは遅い！
H,W=map(int,input().split())
S=[]
for i in range(H):
    s=input()
    S.append(s)
T=[]
for i in range(H):
    t=input()
    T.append(t)

s_rev=[]
t_rev=[]
for i in range(W):
    tmp=''
    tmp2=''
    for j in range(H):
        tmp+=S[j][i]
        tmp2+=T[j][i]
    s_rev.append(tmp)
    t_rev.append(tmp2)

from collections import Counter
cnt_t=Counter()
cnt_s=Counter()
for t in t_rev:
    cnt_t[t]+=1
for s in s_rev:
    cnt_s[s]+=1

for i in range(W):
    if cnt_t[t_rev[i]] != cnt_s[t_rev[i]]:
        print('No')
        exit()

print('Yes')



