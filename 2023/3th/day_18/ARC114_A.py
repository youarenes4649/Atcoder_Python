import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
#素数の約数だけ
from math import gcd
def Eratosthenes(N):
    # 素数であるかの判定リスト
    IsPrime=[True]*(N+1)

    # i=2,3,4,...
    i=2
    # i≤√Nまで⇔i^2≤Nまで
    while i**2<=N:
        # iが素数でなければ
        if IsPrime[i]==False:
            # 次のiへ
            i+=1
            continue
        
        # k=2,3,4,...
        k=2
        while i*k<=N:
            # iの倍数は素数でない
            IsPrime[i*k]=False
            # 次のkへ
            k+=1

        # 次のkへ
        i+=1

    # 素数リスト
    PList=[]

    # i=2~N
    for i in range(2,N+1):
        # iが素数ならば
        if IsPrime[i]==True:
            # リストへ入れる
            PList.append(i)

    # リストを返す
    return PList

def main():
    N = ii()
    X = li()
    
    p_ls = Eratosthenes(50)
    ans = 10 ** 20
    for i in range(1,1 << len(p_ls)):
        Y = 1
        for j in range(len(p_ls)):
            if (i >> j) & 1 == 1:
                Y *= p_ls[j]
        check = True
        for x in X:
            if gcd(x,Y) == 1:
                check = False
                break
            
        if check:
            ans = min(ans,Y)
        
    print(ans)
        
 
if __name__ == '__main__':
    main()