N,X,Y,Z=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
from collections import defaultdict
A_new=defaultdict(list)
B_new=defaultdict(list)
AB_new=defaultdict(list)
goukaku=[False]*N
for i in range(N):
    A_new[A[i]].append(i)
    B_new[B[i]].append(i)
    AB_new[A[i]+B[i]].append(i)

a=sorted(A_new.items(),reverse=True)
b=sorted(B_new.items(),reverse=True)
ab=sorted(AB_new.items(),reverse=True)
x=0
a_new=[]
for an in a:
    an_ls=an[1]
    a_new.extend(an_ls)
b_new=[]
for bn in b:
    bn_ls=bn[1]
    b_new.extend(bn_ls)
    
ab_new=[]
for abn in ab:
    abn_ls=abn[1]
    ab_new.extend(abn_ls)

for x in range(X):
    number=a_new[x]
    goukaku[number]=True

y=0
i=0
while y<Y:
    number=b_new[i]
    if goukaku[number]:
        i+=1
        continue

    goukaku[number]=True
    y+=1

z=0
i=0
while z<Z:
    number=ab_new[i]
    if goukaku[number]:
        i+=1
        continue

    goukaku[number]=True
    z+=1


for n in range(N):
    if goukaku[n]:
        print(n+1)




    
