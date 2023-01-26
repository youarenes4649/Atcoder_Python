N=int(input())
A=list(map(int,input().split()))

#a=2**xi * 3**yi *zi になるから最小のxi,yiに合わせる必要がある
#zi!=zjだった場合-1を表示
#全ての最大公約数を求める
from math import gcd

GCD=A[0]
for i in range(N):
    GCD=gcd(GCD,A[i])

for i in range(N):#GCDでAの要素を割ることで残りを数える
    A[i]=A[i]//GCD

#GCDで割るから残りが1*2**x*3**yになっていないとおかしいのか
ans=0
for a in A:
    while a%2==0:
        a//=2
        ans+=1


    while a%3==0:
        a//=3
        ans+=1


    if a!=1:

        print(-1)
        exit()


print(ans)