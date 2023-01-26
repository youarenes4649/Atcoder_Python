N,L,R=map(int,input().split())
a=list(map(int,input().split()))
f=[0]*(N+1)#Lの最小値
g=[0]*(N+1)#Rの最小値
h=[0]*(N+1)

for i in range(1,N+1):
    f[i]=min(f[i-1]+a[i-1],L*i)
    g[i]=min(g[i-1]+a[N-i],R*i)

for i in range(N+1):
    #もしg[n-2]でもRが１個だけ使われた場合が最小値の時も格納されている。
    h[i]=f[i]+g[N-i]# ひだりからLがi個のときは右からRはN-i子使用したときの最小値

print(min(h))


    
    

        