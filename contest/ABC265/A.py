X,Y,N=map(int,input().split())
if N<3:
    print(X*N)

else:
    cnt=(N//3)*Y
    cnt2=N*X
    print(min(cnt+(N-(N//3)*3)*X,cnt2))
    


    