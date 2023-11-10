def main():
    import bisect
    from collections import defaultdict
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    sum_k = sum(A[:K])
    sum_s = sum(sorted(A)[::-1][:K])
    if sum_s == sum_k: #Kまでの総和が最大だったら無理
        exit(print(-1))
        
#----------------------------------------------------------------#
    #まずはそれぞれの位置を見つけておく　なるべく左側に寄っているのがいい
    loc = defaultdict(int) # 数字の場所
    for i in range(N):
        if i < K  :
            continue
        if loc[A[i]] == False:
            loc[A[i]] = i
            
    ans = 10 ** 20
    L = A[:K]
    A_max = [A[K]]
    for i in range(K+1, N):
        A_max.append(max(A_max[-1], A[i]))
    #print(A_max)
    
    for l in range(K):
        al = L[l]
        r = bisect.bisect_right(A_max,al)
        if r == len(A_max): #その値は変える必要がないので
            continue
        if A_max[r] <= al:
            continue
        r = loc[A_max[r]]
        ans = min(ans,r - l)
    if ans == 10**20:
        print(-1)
    else:
        print(ans)
        
  
if __name__ == '__main__':
    main()