#やっていることは同じなんだけどなあ これをもっと見やすいやり方でする
def main():
    from collections import defaultdict
    import bisect

    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    S = sum(A[:K])
    
    #好きな回数できるのでどんなスコアにもできる　S＋1 にすればいいから　一番近いやつかつ
    # A[:k] の中で一番小さいやつも
    L = A[:K]
    R = A[K:]
    
    loc = defaultdict(int)
    for i in range(N-K):
        if loc[R[i]] == 0:
            loc[R[i]] = K + i

    R.sort() # 二分探索するために使用する
    ans = 10**20
    for i in range(K-1,-1,-1):
        num = L[i]
        idx = bisect.bisect_right(R,num)
        if idx == N - K: #もうすでに大きい
            continue
        
        if num < R[idx]: #スコアを加算できる
            ans = min(ans, loc[R[idx]] - i)
        
    if ans == 10**20:
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()