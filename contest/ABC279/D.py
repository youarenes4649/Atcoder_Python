A,B=map(int,input().split())
from decimal import Decimal, ROUND_HALF_UP
 
def func(g,b,a):
    return (g-1)*(b)+(a)/(g**0.5)
 
#(2)関数fの最小値を探したい閉区間の両端をl,rと置く(l<=r)
l,r=1,10**18
#(3)誤差が10^-8を下回るまでwhile文を回す
while l+2<r:
    #(4)オーバーフローしないように以下のように三等分点を置く
    c1=l+(r-l)//3
    c2=r-(r-l)//3
    #(5)更新を行う
    if func(c1,B,A)<func(c2,B,A):
        r=c2
    else:
        l=c1
 
 
ans=10**20
 
res=min(func(x,B,A) for x in range(l,r+1))
print(Decimal(res))