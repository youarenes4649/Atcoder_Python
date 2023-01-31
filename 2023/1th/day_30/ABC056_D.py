#dp で解いてみる
def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    
    ok = -1
    ng = N
    
    def is_ok(n):
        dp = [False] * (K + 1)
        dp[0] = True
        
        for i in range(N):
            if n == i: # 使用しない番号はスルー
                continue
            
            for j in range(K ,A[i]-1,-1):
                dp[j] = dp[j] | dp[j - A[i]]
                
        
        if K <= A[n]: #need
            return True 
        
        for i in range(K-A[n],K):
            if dp[i]: 
                return True 

        return False
    
    
    while ng - ok > 1:
        mid = (ok + ng) // 2
        
        if is_ok(mid):
            ng = mid
        else:
            ok = mid
            
    print(ng)
            
            
if __name__ == '__main__':
    main()