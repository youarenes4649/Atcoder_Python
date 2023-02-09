
def main():
    def is_ok(x):
        times = []
        for i in range(N):
            t = (x - H[i] ) // S[i]
            times.append(t)
        times.sort()
        for i in range(N):
            if times[i] < N:
                return False
            
        return True
                
    
    N = int(input())
    H,S = [],[]
    for i in range(N):
        h,s = map(int,input().split())
        H.append(h)
        S.append(s)
        
    ok = 10**18
    ng = 0
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
     
    print(ok)
            
if __name__ == '__main__':
    main()