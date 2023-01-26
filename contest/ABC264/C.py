H,W=map(int,input().split())

A=[]
for i in range(H):
    a=list(map(int,input().split()))
    A.append(a)

H2,W2=map(int,input().split())
B=[]
for i in range(H2):
    b=list(map(int,input().split()))
    B.append(b)

if H==H2 and W==W2:
    if A==B:
        print('Yes')

    else:
        print('No')

    exit()
for i in range(1,1<<H):
    use_gyow=[]
    for ii in range(H):
        if (i>>ii)&1==1:
            use_gyow.append(ii)
    
    for j in range(1,1<<W):
        use_retu=[]
        ans_grid=[]
        for jj in range(W):
            if (j>>jj)&1==1:
                use_retu.append(jj)

        for i,gyou in enumerate(use_gyow):
            tmp=[]
            for j,retu in enumerate(use_retu):
                tmp.append(A[gyou][retu])
            ans_grid.append(tmp)            
        

        if ans_grid==B:
            print('Yes')
            exit()


print('No')
        

        


