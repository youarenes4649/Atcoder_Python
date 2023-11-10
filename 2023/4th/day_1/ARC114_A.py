import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
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
    P = Eratosthenes(51)
    ans = 10 ** 20
    for i in range(1 << len(P)):
        use_list = []
        for j in range(len(P)):
            if (i >> j) & 1:
                use_list.append(P[j])
        
        check = [False] * N
        for p in use_list:
            for j in range(N):
                if X[j] % p == 0:
                    check[j] = True
        
        if all(check):
            tmp_ans = 1
            for p in use_list:
                tmp_ans *= p
                
            ans = min(ans,tmp_ans)
        
    print(ans)
                
            
            
if __name__ == '__main__':
    main()