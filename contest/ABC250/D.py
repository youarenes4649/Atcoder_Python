def Eratosthenes(N):

    IsPrime=[True]*(N+1)

    i=2
    
    while i**2<=N:
        if IsPrime[i]==False:
            i+=1
            continue


        k=2
        while i*k<=N:
            IsPrime[i*k]=False
            k+=1



        i+=1

    prime=[]
    for i in range(2,N+1):

        if IsPrime[i]:
            prime.append(i)

    return prime


N=int(input())
#10**6以下の素数のリストを作成
P_ls=Eratosthenes(10**6)
ans=0

k=len(P_ls)-1 #素数リストの最後の番号
for i in range(len(P_ls)):

    while 0<k and N<P_ls[i]*(P_ls[k]**3):#ここで続かないようにしてることで計算量早くする
        k-=1



    if k<=i:
        break


    ans+=k-i


print(ans)

    






            



    
