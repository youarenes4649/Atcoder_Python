def main():
    
    def is_ok(x):
        judge = M #既にxニタしている
        if x < P:
            return True
        if A[x] + M < A[P-1]:
            return False
        
        for i in range(P-1):
            judge += M 
            
        for i in range(x+1,N):
            judge += M
            
        for i in range(P,x):
            judge += max(0,A[x] + M - A[i])
        
        if judge >= M * V:#そんなジャッジできないので
            return True
        else:
            return False

    N,M,V,P = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    ok = N
    ng = 0
    while ok - ng > 1:
        mid = (ok + ng) // 2
        
        if is_ok(mid-1):
            ng = mid
        else:
            ok = mid
    print(ok)
if __name__ == '__main__':
    main()