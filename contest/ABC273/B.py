X,K=map(int,input().split())

for i in range(K):
    str_X=str(X)
    if len(str_X)-(i+1)<0:
        break
    now=str_X[len(str_X)-(i+1)]
    if int(now)>=5:
        X+=10**(i+1)
        X-=int(now)*(10**(i))

    else:
        X-=int(now)*(10**i)

 
print(X)

    
        