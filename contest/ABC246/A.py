x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())

Sx=set()
Sy=set()
ansx=[x1,x2,x3]
ansy=[y1,y2,y3]
cntx=1
cnty=1
ans=[]
for  x in ansx:
    if ansx.count(x)==1:
        ans.append(x)

for  y in ansy:
    if ansy.count(y)==1:
        ans.append(y)

print(*ans)