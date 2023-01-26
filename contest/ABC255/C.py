X,A,D,N=map(int,input().split())
#単調増加、もしくは単調減少の２通りになるなら一通りに直して単調増加にする
#そうすることによってその後の処理が楽
if D==0:
    print(abs(X-A))

else:
    if D<0:
        A=A+(N-1)*D
        D*=-1

    mi=A
    mx=A+(N-1)*D

    if X>=mx:
        print(X-mx)
        exit()

    if X<=mi:
        print(mi-X)
        exit()

    else:
        ng=0
        ok=N
        while ok-ng>1:
            mid=(ok+ng)//2
            if X>A+(mid)*D:
                ng=mid

            else:
                ok=mid

        ans=min(abs(X-(A+D*(ok))),abs(X-(A+D*(ok-1))))
        print(ans)

    

    
    

