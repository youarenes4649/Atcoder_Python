N=int(input())

if N==0:
    print(0)
    exit()

def f(a,b):
    return a**3+a*(b**2)+b*(a**2)+b**3


ans=10**20
for a in range(10**6):#片方を変数にして片方を二分探索！！！！！
    ng=-1
    ok=10**6+100
    while (ok-ng>1):
        mid=(ok+ng)//2
        if (N<=f(a,mid)) :
            ok=mid

        else:
            ng=mid

    ans=min(ans,f(a,ok))

print(ans)

    