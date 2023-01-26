S=[]
corn=[]
import math

def get_distance(d1,d2):
    x1,y1=d1
    x2,y2=d2
    d = (x2 - x1) ** 2 + (y2 - y1) ** 2
    return d
for i in range(9):
    s=input()
    for k,j in enumerate(s):
        if j=='#':
            corn.append((i,k))
    S.append(s)
ans=0
for i in range(len(corn)-3):
    for j in range(i+1,len(corn)-2):
        for k in range(j+1,len(corn)-1):
            for l in range(k+1,len(corn)):

                d1=get_distance(corn[i],corn[j])
                d2=get_distance(corn[j],corn[k])
                d3=get_distance(corn[k],corn[l])
                d4=get_distance(corn[l],corn[i])
                d5=get_distance(corn[j],corn[l])
                d6=get_distance(corn[i],corn[k])
                d_ls=[d1,d2,d3,d4,d5,d6]
                d_ls.sort()
                if d_ls[0]==d_ls[1]==d_ls[2]==d_ls[3]:
                    if d_ls[4]==d_ls[5]:
                        ans+=1

print(ans)

                

                

