h1,h2,h3,w1,w2,w3=map(int,input().split())
ans=0

for H11 in range(1,30):
    for H12 in range(1,30):
        for H21 in range(1,30):
            for H22 in range(1,30):
                h13=h1-H11-H12
                h23=h2-H21-H22
                h33=w3-h13-h23
                h31=w1-H11-H21
                h32=w2-H22-H12
                if min(h13,h33,h32,h31,h23)>0 :
                    if h31+h32+h33==h3:
                        ans+=1
                    
print(ans)          
#元の値から引いておくべきだった