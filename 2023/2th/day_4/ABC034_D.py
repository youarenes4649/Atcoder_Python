
def main():
    def check(x):
        cand = []
        for i in range(N):
            w,p = W[i],P[i]
            c = (w * p - w * x)/100
            cand.append(c)
        cand.sort(reverse=True)
        if sum(cand[:K]) >= 0 :
            return True
        
        else:
            return False
        
        
    N,K = map(int,input().split())
    W = []
    P = []
    for i in range(N):
        w,p = map(int,input().split())
        W.append(w)
        P.append(p)
    ok = 100
    ng = 0
    while ok - ng > 10**(-9):
        mid = (ok + ng)/2
        
        if check(mid):
            ng = mid
        
        else:
            ok = mid
            
    print(ng)
            
    
        
    
        
if __name__ == '__main__':
    main()